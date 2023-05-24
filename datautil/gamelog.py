from datautil.common import path_to_save_base
import re

def load_logs(savefilename):
    #TODO: refactor
    fn = []
    for findex in range(1,14188):
        try:
            fn += [x[0:4] + str(findex) + x[4:] for x in open(path_to_save_base(savefilename) + "/news/txt/leagues/log_{}.txt".format(findex)).readlines()]
        except:
            pass
    return [ln.strip() for ln in fn]

def result_parse(ln):
    if "Fly out" in ln:
        return "FO"
    if "Base on Balls" in ln:
        return "BB"
    if "Strikes out" in ln:
        return "SO"
    if "Ground out" in ln or "Grounds out" in ln:
        return "GO"
    if "Hit by Pitch" in ln:
        return "HBP"
    if "Grounds into double play" in ln or "Grounds into DOUBLE play" in ln:
        return "GIDP" # 땅볼 - 병살타
    if "<b>SINGLE</b>" in ln:
        return "H1"
    if "<b>DOUBLE</b>" in ln:
        return "H2"
    if "<b>TRIPLE</b>" in ln:
        return "H3"
    if "HOME RUN</b>" in ln:
        return "HR"
    if "Intentional Walk" in ln:
        return "IBB"
    if "Reached on error" in ln or "Reached via error" in ln:
        return "ERR"
    if "Fielders Choice" in ln:
        return "FielderC" # 야수 선택
    if "Grounds into fielders choice" in ln:
        return "FielderC" # 위에랑 차이점?
    if "Sac Bunt" in ln:
        if "batter safe" in ln: # bunt hit
            return "H1-SacBunt"
        return "SacBunt"
    if "Single, Error in" in ln:
        return "H1+Err"
    if "Bunt for hit " in ln:
        if "batter safe" in ln:
            return "H1-Bunt" # to make sure all runner safe
        return "GO-Bunt"
    if "Bunt - Flyout" in ln:
        return "FO-Bunt"
    if "Squeeze Bunt" in ln:
        if "runner OUT" in ln: # bunt fail
            return "FC-sqzbunt"
        if "runner scores, batter safe" in ln: # hit
            return "H1-SqzBunt"
        return "SacBunt-SqzBunt"
    if "Reaches on Catchers interference" in ln: 
        return "ERR-Inference" # 스윙방해
    
    if "Pickoff Throw " in ln or "Pickoff Play " in ln:
        return "PICKOFF" # 견제사
    if "is caught stealing " in ln:
        return "STEALFAIL" # 도루실패
    
    if re.search("3-[0-2]: Ball", ln) != None:
        # actually base on balls, not sure why it's just expressed as a ball
        return "BB"
    
    if "SINGLE, rundown," in ln:
        return "H1+RunDown"
    
    if "SINGLE, but batter called out on appeal for missing first base!" in ln:
        return "H1+MissingBase" # 1루 안밟아서 아웃
    
    if "Bunted foul, Strikeout!" in ln or "Bunt missed, Strikeout!" in ln:
        return "SO-Bunt" # 쓰리번트실패 삼진아웃
    return None

def findPlayerId(ln):
    match = re.search("player_(\d+).html",ln)
    return int(match.group(1))

def simplify_game_logs(gamelogs):
    result_list = []

    for i in range(len(gamelogs)):
        ln = gamelogs[i]
        
        if "Pitching: " in ln or ("Top of the " in ln or "Bottom of the " in ln) and "Pitching for" in ln: # inning start with pitcher introd
            try:
                pitcher_id = findPlayerId(ln)
            except Exception as E:
                pitcher_id = None
            batter_id = None
            
        if "Batting: " in ln or "Pinch Hitting:" in ln or re.search("Top of the [1-9a-z]* over", ln) != None: # new batter or inning end
            if batter_id != None:
                # find prev result
                found = False
                for j in range(i-1,-1,-1):
                    # TODO: double check following logic
                    if re.search(r"\[%N\]\d+\s*\d-\d", gamelogs[j]) != None or \
                        re.search("Pickoff (Play|Throw) .*(OUT|Out)", gamelogs[j]) != None or \
                        re.search("is caught stealing [1-3a-z]* base", gamelogs[j]) != None or \
                        re.search("SINGLE, rundown,", gamelogs[j]) != None or \
                        re.search("SINGLE, but batter called out on appeal for missing first base!", gamelogs[j]) != None: # result
                        
                        result = result_parse(gamelogs[j])
                        
                        result_list.append({
                            'result': result,
                            'pitcher': pitcher_id,
                            'batter': batter_id,
                            'is_pa': result not in ("PICKOFF", "STEALFAIL"),
                            'is_ab': result not in ("PICKOFF", "STEALFAIL", "BB", "IBB", "HBP"),
                        })

                        found = True
                        break
                if found == False:
                    raise Exception("couldn't find result")
            if "Batting: " in ln or "Pinch Hitting:" in ln:
                # new batter
                batter_id = findPlayerId(ln)
    
    return result_list