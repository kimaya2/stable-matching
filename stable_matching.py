
preferred_rankings_men = {
    'raj' : ['lisa','simran','anjali'],
    'rahul' : ['anjali','lisa','simran'],
    'yash' : ['anjali','simran','lisa'] 
}

preferred_rankings_women = {
    'anjali' : ['raj','rahul', 'yash'],
    'lisa' : ['yash','raj','rahul'],
    'simran' : ['yash','rahul','raj'] 
}

#keeps track of people that may end up together
tentative_engagements = []

#men who do not have a partner yet
free_men = []

def init_free_men():
    for men in preferred_rankings_men.keys():
        free_men.append(men)

def begin_matching(man):
    print("Matching for "+man)
    for woman in preferred_rankings_men[man]:

        taken_match = [couple for couple in tentative_engagements if woman in couple]

        #woman is not matched with anyone
        if len(taken_match) == 0:
            tentative_engagements.append([man,woman])
            free_men.remove(man)
            print(man+" no longer free and tentatively engaged to "+woman)
            break

        #woman already matched with someone and comparision between current and potential partner
        elif len(taken_match) > 0:
            print(woman+" taken already")
            current_guy = preferred_rankings_women[woman].index(taken_match[0][0])
            potential_guy = preferred_rankings_women[woman].index(man)

            if current_guy < potential_guy:
                print(woman+" satisfied with "+taken_match[0][0])
            else:
                print(woman+" better off with "+man)
                print(taken_match[0][0]+" is free again")

                free_men.remove(man)
                free_men.append(taken_match[0][0])
                taken_match[0][0] = man
                break

def stable_matching():
    while len(free_men) > 0:
        for man in free_men:
            begin_matching(man)

if __name__ == "__main__":
    init_free_men()
    stable_matching()