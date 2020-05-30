import numpy as np
import textwrap


##################### Functions ##########

def playerboard(All_Numbers, player_1_pawns, player_1_crowns, player_2_pawns, player_2_crowns):
    ######### Mark players
    for i in All_Numbers:
        if (i in player_1_pawns):
            All_Numbers[i - 1] = "\u2187"
    for i in All_Numbers:
        if (i in player_1_crowns):
            All_Numbers[i - 1] = "\u2188"
    for j in All_Numbers:
        if (j in player_2_pawns):
            All_Numbers[j - 1] = "\u25E5"
    for j in All_Numbers:
        if (j in player_2_crowns):
            All_Numbers[j - 1] = "\u25FC"
    # blocked values:
    for b in All_Numbers:
        if (b == 1 or b == 7 or b == 43 or b == 49):
            All_Numbers[b - 1] = " "

    BOLD = '\033[1m'
    END = '\033[0m'

#    print(All_Numbers[0:7])
#    print('{}{}{}'.format(BOLD, All_Numbers[7:14], END))
    fixed_string = "{0:^45}".format(str(All_Numbers[0:7]))
    print(fixed_string)
    fixed_string = "{0:^45}".format(str(All_Numbers[7:14]))
    print(fixed_string)
    #print(All_Numbers[7:14])
    fixed_string = "{0:^45}".format(str(All_Numbers[14:21]))
    print(fixed_string)
    #print(All_Numbers[14:21])
    fixed_string = "{0:^45}".format(str(All_Numbers[21:28]))
    print(fixed_string)
    #print(All_Numbers[21:28])
    fixed_string = "{0:^45}".format(str(All_Numbers[28:35]))
    print(fixed_string)
    #print(All_Numbers[28:35])
    fixed_string = "{0:^45}".format(str(All_Numbers[35:42]))
    print(fixed_string)
    #print(All_Numbers[35:42])
    fixed_string = "{0:^45}".format(str(All_Numbers[42:49]))
    print(fixed_string)
    #print(All_Numbers[42:49])

    return

def checkpossiblemoves_p1(player_1_selected_node, player_1_pawns_and_crowns,
                              player_2_pawns_and_crowns, sequence_of_moves):
        ############begin center square
        if ((player_1_selected_node >= 9 and player_1_selected_node <= 13) or
                (player_1_selected_node >= 16 and player_1_selected_node <= 20) or
                (player_1_selected_node >= 23 and player_1_selected_node <= 27) or
                (player_1_selected_node >= 30 and player_1_selected_node <= 34) or
                (player_1_selected_node >= 37 and player_1_selected_node <= 41)):

            up = player_1_selected_node - 7
            down = player_1_selected_node + 7
            left = player_1_selected_node - 1
            right = player_1_selected_node + 1
            complete_move_options = [up, down, left, right]
        ############end center square

        ################begin left numbers
        elif ((player_1_selected_node == 15)
              or (player_1_selected_node == 22)
              or (player_1_selected_node == 29)):

            up = player_1_selected_node - 7
            down = player_1_selected_node + 7
            right = player_1_selected_node + 1
            complete_move_options = [up, down, right]

        elif ((player_1_selected_node == 8)):

            down = player_1_selected_node + 7
            right = player_1_selected_node + 1
            complete_move_options = [down, right]

        elif ((player_1_selected_node == 36)):

            up = player_1_selected_node - 7
            right = player_1_selected_node + 1
            complete_move_options = [up, right]

        #################end left numbers

        ################begin down numbers
        elif ((player_1_selected_node == 45)
              or (player_1_selected_node == 46)
              or (player_1_selected_node == 47)):

            up = player_1_selected_node - 7
            left = player_1_selected_node - 1
            right = player_1_selected_node + 1
            complete_move_options = [up, left, right]

        elif ((player_1_selected_node == 44)):

            up = player_1_selected_node - 7
            right = player_1_selected_node + 1
            complete_move_options = [up, right]

        elif ((player_1_selected_node == 48)):

            up = player_1_selected_node - 7
            left = player_1_selected_node - 1
            complete_move_options = [up, left]

        #################end down numbers

        ################begin right numbers
        elif ((player_1_selected_node == 21)
              or (player_1_selected_node == 28)
              or (player_1_selected_node == 35)):

            up = player_1_selected_node - 7
            down = player_1_selected_node + 7
            left = player_1_selected_node - 1
            complete_move_options = [up, down, left]

        elif ((player_1_selected_node == 14)):

            down = player_1_selected_node + 7
            left = player_1_selected_node - 1
            complete_move_options = [down, left]

        elif ((player_1_selected_node == 42)):

            up = player_1_selected_node - 7
            left = player_1_selected_node - 1
            complete_move_options = [up, left]

        #################end right numbers

        ################begin up numbers
        elif ((player_1_selected_node == 3)
              or (player_1_selected_node == 4)
              or (player_1_selected_node == 5)):

            down = player_1_selected_node + 7
            left = player_1_selected_node - 1
            right = player_1_selected_node + 1
            complete_move_options = [down, left, right]

        elif ((player_1_selected_node == 2)):

            down = player_1_selected_node + 7
            right = player_1_selected_node + 1
            complete_move_options = [down, right]

        elif ((player_1_selected_node == 6)):

            down = player_1_selected_node + 7
            left = player_1_selected_node - 1
            complete_move_options = [down, left]

        #################end up numbers

        else:
            print("Case not considered.")

        #################################################

        moves_to_be_removed = []
        for move in complete_move_options:

            if move in (
                    player_1_pawns_and_crowns + player_2_pawns_and_crowns):  # if the potential node u,d,l, or r is occupied
                moves_to_be_removed.append(move)
                #print("Piece cannot move in direction: " + str(move))
                ###### need to add case in which no moves available
            else:
                nothing = 0
                # print("Piece can move in direction: " + str(move))
        print("Moves to be removed: " + str(moves_to_be_removed))

        for move in complete_move_options:
            if ((len(sequence_of_moves) > 0) and
                    (sequence_of_moves[-1] == str("p1: ") + str(move) + str("->") + str(player_1_selected_node))):
                moves_to_be_removed.append(move)
                print("Prior Move in Sequence: " + str(sequence_of_moves[-1]))
                print(str([move]) + " is removed because it was a previous move.")

        print("Complete move options before removal: " + str(complete_move_options))

        for k in moves_to_be_removed:
            complete_move_options.remove(k)
        print("Complete move options AFTER removal: " + str(complete_move_options))
        print("")

        return complete_move_options

def player_1_moveaction(All_Numbers, player_1_pawns, player_1_crowns,
                        player_2_pawns, player_2_crowns, sequence_of_moves):

    ####################### Checking Nodes available for move #################
    player_1_pawn_or_crown_selected_for_move = 0
    pseudovar_player_1_pawns_and_crowns = player_1_pawns + player_1_crowns
    while player_1_pawn_or_crown_selected_for_move < 1:

        r1 = np.random.randint(0, len(pseudovar_player_1_pawns_and_crowns), 1)
        # r1 = [0,0] #fixes a selected node
        player_1_selected_node = pseudovar_player_1_pawns_and_crowns[r1[0]]
        print("Player Selected Node: " + str(player_1_selected_node))

        ######### Check possible moves for player 1 selected node#####
        check_possible_moves_p1 = checkpossiblemoves_p1(player_1_selected_node,
                                                        player_1_pawns + player_1_crowns,
                                                        player_2_pawns + player_2_crowns,
                                                        sequence_of_moves)

        complete_move_options = check_possible_moves_p1
        if len(complete_move_options) > 0:
            ####################################
            ############ randomly picking a move direction
            r2 = np.random.randint(0, len(complete_move_options), 1)
            move_chosen = complete_move_options[r2[0]]  # ex. =2, from 9

            ####### remove number from pawn or crown from set
            for i in (player_1_pawns):  # looking at all numbers in player's pawn set
                if (i == player_1_selected_node):
                    player_1_pawns.remove(i)
                    player_1_pawns.append(move_chosen)
                    ######### add regular number back to board
                    All_Numbers[i - 1] = player_1_selected_node

            for i in (player_1_crowns):  # looking at all numbers in player's crown set
                if (i == player_1_selected_node):
                    player_1_crowns.remove(i)
                    player_1_crowns.append(move_chosen)
                    ######### add regular number back to board
                    All_Numbers[i - 1] = player_1_selected_node

            sequence_of_moves.append("p1: " + str(player_1_selected_node) + "->" + str(move_chosen))
            print("Sequence of Moves: " + textwrap.fill(str(sequence_of_moves), 30))
            ####################################
            action = 1 ##increments the action in the output
            player_1_pawn_or_crown_selected_for_move = 1
        else:
            player_1_pawn_or_crown_selected_for_move = 0
            pseudovar_player_1_pawns_and_crowns.remove(player_1_selected_node)
            if len(pseudovar_player_1_pawns_and_crowns) == 0:
                print("No available nodes for player 1 to select to perform a move.")
                action = 0
                break


    return (All_Numbers, player_1_pawns, player_1_crowns,
            player_2_pawns, player_2_crowns, sequence_of_moves,action)

def checkpossiblemoves_p2(player_2_selected_node, player_1_pawns_and_crowns,
                          player_2_pawns_and_crowns, sequence_of_moves):
    ############begin center square
    if ((player_2_selected_node >= 9 and player_2_selected_node <= 13) or
            (player_2_selected_node >= 16 and player_2_selected_node <= 20) or
            (player_2_selected_node >= 23 and player_2_selected_node <= 27) or
            (player_2_selected_node >= 30 and player_2_selected_node <= 34) or
            (player_2_selected_node >= 37 and player_2_selected_node <= 41)):

        up = player_2_selected_node - 7
        down = player_2_selected_node + 7
        left = player_2_selected_node - 1
        right = player_2_selected_node + 1
        complete_move_options = [up, down, left, right]
    ############end center square

    ################begin left numbers
    elif ((player_2_selected_node == 15)
          or (player_2_selected_node == 22)
          or (player_2_selected_node == 29)):

        up = player_2_selected_node - 7
        down = player_2_selected_node + 7
        right = player_2_selected_node + 1
        complete_move_options = [up, down, right]

    elif ((player_2_selected_node == 8)):

        down = player_2_selected_node + 7
        right = player_2_selected_node + 1
        complete_move_options = [down, right]

    elif ((player_2_selected_node == 36)):

        up = player_2_selected_node - 7
        right = player_2_selected_node + 1
        complete_move_options = [up, right]

    #################end left numbers

    ################begin down numbers
    elif ((player_2_selected_node == 45)
          or (player_2_selected_node == 46)
          or (player_2_selected_node == 47)):

        up = player_2_selected_node - 7
        left = player_2_selected_node - 1
        right = player_2_selected_node + 1
        complete_move_options = [up, left, right]

    elif ((player_2_selected_node == 44)):

        up = player_2_selected_node - 7
        right = player_2_selected_node + 1
        complete_move_options = [up, right]

    elif ((player_2_selected_node == 48)):

        up = player_2_selected_node - 7
        left = player_2_selected_node - 1
        complete_move_options = [up, left]

    #################end down numbers

    ################begin right numbers
    elif ((player_2_selected_node == 21)
          or (player_2_selected_node == 28)
          or (player_2_selected_node == 35)):

        up = player_2_selected_node - 7
        down = player_2_selected_node + 7
        left = player_2_selected_node - 1
        complete_move_options = [up, down, left]

    elif ((player_2_selected_node == 14)):

        down = player_2_selected_node + 7
        left = player_2_selected_node - 1
        complete_move_options = [down, left]

    elif ((player_2_selected_node == 42)):

        up = player_2_selected_node - 7
        left = player_2_selected_node - 1
        complete_move_options = [up, left]

    #################end right numbers

    ################begin up numbers
    elif ((player_2_selected_node == 3)
          or (player_2_selected_node == 4)
          or (player_2_selected_node == 5)):

        down = player_2_selected_node + 7
        left = player_2_selected_node - 1
        right = player_2_selected_node + 1
        complete_move_options = [down, left, right]

    elif ((player_2_selected_node == 2)):

        down = player_2_selected_node + 7
        right = player_2_selected_node + 1
        complete_move_options = [down, right]

    elif ((player_2_selected_node == 6)):

        down = player_2_selected_node + 7
        left = player_2_selected_node - 1
        complete_move_options = [down, left]

    #################end up numbers

    else:
        print("Case not considered.")

    #################################################

    moves_to_be_removed = []
    for move in complete_move_options:

        if move in (
                player_1_pawns_and_crowns + player_2_pawns_and_crowns):  # if the potential node u,d,l, or r is occupied
            moves_to_be_removed.append(move)
            # print("Piece cannot move in direction: " + str(move))
            ###### need to add case in which no moves available
        else:
            nothing = 0
            # print("Piece can move in direction: " + str(move))
    print("Moves to be removed: " + str(moves_to_be_removed))

    for move in complete_move_options:
        if ((len(sequence_of_moves) > 0) and
                (sequence_of_moves[-1] == str("p2: ") + str(move) + str("->") + str(player_2_selected_node))):
            moves_to_be_removed.append(move)
            print("Prior Move in Sequence: " + str(sequence_of_moves[-1]))
            print(str([move]) + " is removed because it was a previous move.")

    print("Complete move options before removal: " + str(complete_move_options))

    for k in moves_to_be_removed:
        complete_move_options.remove(k)
    print("Complete move options AFTER removal: " + str(complete_move_options))
    print("")

    return complete_move_options

def player_2_moveaction(All_Numbers, player_1_pawns, player_1_crowns,
                        player_2_pawns, player_2_crowns, sequence_of_moves):

    ####################### Checking Nodes available for move #################
    player_2_pawn_or_crown_selected_for_move = 0
    pseudovar_player_2_pawns_and_crowns = player_2_pawns + player_2_crowns
    while player_2_pawn_or_crown_selected_for_move < 1:

        r1 = np.random.randint(0, len(pseudovar_player_2_pawns_and_crowns), 1)
        # r1 = [0,0] #fixes a selected node
        player_2_selected_node = pseudovar_player_2_pawns_and_crowns[r1[0]]
        print("Player Selected Node: " + str(player_2_selected_node))

        ######### Check possible moves for player 1 selected node#####
        check_possible_moves_p2 = checkpossiblemoves_p2(player_2_selected_node,
                                                        player_1_pawns + player_1_crowns,
                                                        player_2_pawns + player_2_crowns,
                                                        sequence_of_moves)

        complete_move_options = check_possible_moves_p2
        if len(complete_move_options) > 0:
            ####################################
            ############ randomly picking a move direction
            r2 = np.random.randint(0, len(complete_move_options), 1)
            move_chosen = complete_move_options[r2[0]]  # ex. =2, from 9

            ####### remove number from pawn or crown from set
            for i in (player_2_pawns):  # looking at all numbers in player's pawn set
                if (i == player_2_selected_node):
                    player_2_pawns.remove(i)
                    player_2_pawns.append(move_chosen)
                    ######### add regular number back to board
                    All_Numbers[i - 1] = player_2_selected_node

            for i in (player_2_crowns):  # looking at all numbers in player's crown set
                if (i == player_2_selected_node):
                    player_2_crowns.remove(i)
                    player_2_crowns.append(move_chosen)
                    ######### add regular number back to board
                    All_Numbers[i - 1] = player_2_selected_node

            sequence_of_moves.append("p2: " + str(player_2_selected_node) + "->" + str(move_chosen))
            print("Sequence of Moves: " + textwrap.fill(str(sequence_of_moves), 30))
            ####################################
            action = 1 ##increments the action in the output
            player_2_pawn_or_crown_selected_for_move = 1
        else:
            player_2_pawn_or_crown_selected_for_move = 0
            pseudovar_player_2_pawns_and_crowns.remove(player_2_selected_node)
            if len(pseudovar_player_2_pawns_and_crowns) == 0:
                print("No available nodes for player 2 to select to perform a move.")
                action = 0
                break


    return (All_Numbers, player_1_pawns, player_1_crowns,
            player_2_pawns, player_2_crowns, sequence_of_moves,action)

def promoteplayer2spawns(player_1_pawns, player_1_crowns, player_2_pawns, player_2_crowns
                            , sequence_of_moves,All_Numbers):
    possible_promotions = []
    for i in player_2_pawns:
        if ((i in player_2_pawns) and
                (i - 1 in player_2_pawns) and
                (i - 2 in player_2_pawns)):
            possible_promotions.append([i - 2, i, i - 1])
        elif ((i in player_2_pawns) and
              (i - 1 in player_2_pawns) and
              (i + 1 in player_2_pawns)):
            possible_promotions.append([i - 1, i, i + 1])
        elif ((i in player_2_pawns) and
              (i + 1 in player_2_pawns) and
              (i + 2 in player_2_pawns)):
            possible_promotions.append([i + 1, i, i + 2])
        elif ((i in player_2_pawns) and
              (i - 14 in player_2_pawns) and
              (i - 7 in player_2_pawns)):
            possible_promotions.append([i - 14, i, i - 7])
        elif ((i in player_2_pawns) and
              (i - 7 in player_2_pawns) and
              (i + 7 in player_2_pawns)):
            possible_promotions.append([i - 7, i, i + 7])
        elif ((i in player_2_pawns) and
              (i + 7 in player_2_pawns) and
              (i + 14 in player_2_pawns)):
            possible_promotions.append([i + 7, i, i + 14])

    if (len(possible_promotions) >= 1):
        r6 = np.random.randint(0, len(possible_promotions), 1)
        print("Possible Promotions: " + str(possible_promotions))
        selected_triple_for_promotion = possible_promotions[r6[0]]
        print("Selected triple for promotion: " + str(selected_triple_for_promotion))
        print("Player 2 Pawns and Crowns" + str(player_2_pawns)
              + str(player_2_crowns))

        for i in selected_triple_for_promotion:
            player_2_pawns.remove(i)
            ######### add regular number back to board
            All_Numbers[i - 1] = i


        q = np.mean(selected_triple_for_promotion)
        player_2_crowns.append(int(q))
        sequence_of_moves.append("p1Pp2: " + str(np.mean(selected_triple_for_promotion)))
        action = 1
        print("$$$$$$$$$$$$$$$$$$")
        print("$$$$$$$$$$$$$$$$$$")

    else:
        print("None of player 2's pawns can be promoted")
        action = 0

    return (player_1_pawns, player_1_crowns, player_2_pawns,
            player_2_crowns, sequence_of_moves, action,All_Numbers)

def player1swaps(All_Numbers, player_1_pawns, player_1_crowns, player_2_pawns, player_2_crowns
                 , sequence_of_moves):
    reasonable_swap_player_1_crowns = []

    if (len(player_1_crowns) >= 1):
        for i in player_1_crowns:
            if (((i - 7) in (player_2_pawns + player_2_crowns)) and ((i - 7) in [2, 3, 4, 5, 6])) or (
                    ((i + 1) in (player_2_pawns + player_2_crowns)) and ((i + 1) in [14, 21, 28, 35, 42])) or (
                    ((i + 7) in (player_2_pawns + player_2_crowns)) and ((i + 7) in [44, 45, 46, 47, 48])) or (
                    ((i - 1) in (player_2_pawns + player_2_crowns)) and ((i - 1) in [8, 15, 22, 29, 36])):
                reasonable_swap_player_1_crowns.append(i)

        if (len(reasonable_swap_player_1_crowns) >= 1):
            r7 = np.random.randint(0, len(reasonable_swap_player_1_crowns), 1)
            player_1_crown_selected = reasonable_swap_player_1_crowns[r7[0]]
            i = player_1_crown_selected
            #action = 1  ##strange place to put this

            if (((i - 7) in (player_2_pawns + player_2_crowns)) and (
                    (i - 7) in [2, 3, 4, 5, 6])):  ###doesn't consider bottom/horiz of cross
                if (((i - 7) in player_2_pawns) and sequence_of_moves[-1] != ("p1Sp2P: " + str(i - 7) + "<->" + str(i))):
                    player_1_crowns.remove(i)
                    All_Numbers[i - 1] = i
                    player_2_pawns.remove(i - 7)
                    All_Numbers[(i - 7) - 1] = i - 7
                    player_1_crowns.append(i - 7)
                    player_2_pawns.append(i)
                    sequence_of_moves.append("p1Sp2P: " + str(i) + "<->" + str(i - 7))
                    action = 1
                elif (((i - 7) in player_2_crowns) and sequence_of_moves[-1] != ("p1Sp2C: " + str(i - 7) + "<->" + str(i))):
                    player_1_crowns.remove(i)
                    All_Numbers[i - 1] = i
                    player_2_crowns.remove(i - 7)
                    All_Numbers[(i - 7) - 1] = i - 7
                    player_1_crowns.append(i - 7)
                    player_2_crowns.append(i)
                    sequence_of_moves.append("p1Sp2C: " + str(i) + "<->" + str(i - 7))
                    action = 1
            elif (((i + 1) in (player_2_pawns + player_2_crowns)) and ((i + 1) in [14, 21, 28, 35, 42])):
                if (((i + 1) in player_2_pawns) and sequence_of_moves[-1] != ("p1Sp2P: " + str(i + 1) + "<->" + str(i))):
                    player_1_crowns.remove(i)
                    All_Numbers[i - 1] = i
                    player_2_pawns.remove(i + 1)
                    All_Numbers[(i + 1) - 1] = i + 1
                    player_1_crowns.append(i + 1)
                    player_2_pawns.append(i)
                    sequence_of_moves.append("p1Sp2P: " + str(i) + "<->" + str(i + 1))
                    action = 1
                elif (((i + 1) in player_2_crowns) and sequence_of_moves[-1] != ("p1Sp2C: " + str(i + 1) + "<->" + str(i))):
                    player_1_crowns.remove(i)
                    All_Numbers[i - 1] = i
                    player_2_crowns.remove(i + 1)
                    All_Numbers[(i + 1) - 1] = i + 1
                    player_1_crowns.append(i + 1)
                    player_2_crowns.append(i)
                    sequence_of_moves.append("p1Sp2C: " + str(i) + "<->" + str(i + 1))
                    action = 1
            elif (((i + 7) in (player_2_pawns + player_2_crowns)) and (
                            (i + 7) in [44, 45, 46, 47, 48])):
                if (((i + 7) in player_2_pawns) and sequence_of_moves[-1] != ("p1Sp2P: " + str(i + 7) + "<->" + str(i))):
                    player_1_crowns.remove(i)
                    All_Numbers[i - 1] = i
                    player_2_pawns.remove(i + 7)
                    All_Numbers[(i + 7) - 1] = i + 7
                    player_1_crowns.append(i + 7)
                    player_2_pawns.append(i)
                    sequence_of_moves.append("p1Sp2P: " + str(i) + "<->" + str(i + 7))
                    action = 1
                elif (((i + 7) in player_2_crowns) and sequence_of_moves[-1] != ("p1Sp2C: " + str(i + 7) + "<->" + str(i))):
                    player_1_crowns.remove(i)
                    All_Numbers[i - 1] = i
                    player_2_crowns.remove(i + 7)
                    All_Numbers[(i + 7) - 1] = i + 7
                    player_1_crowns.append(i + 7)
                    player_2_crowns.append(i)
                    sequence_of_moves.append("p1Sp2C: " + str(i) + "<->" + str(i + 7))
                    action = 1
            elif (((i - 1) in (player_2_pawns + player_2_crowns)) and ((i - 1) in [8, 15, 22, 29, 36])):
                if (((i - 1) in player_2_pawns) and sequence_of_moves[-1] != ("p1Sp2P: " + str(i - 1) + "<->" + str(i))):
                    player_1_crowns.remove(i)
                    All_Numbers[i - 1] = i
                    player_2_pawns.remove(i - 1)
                    All_Numbers[(i - 1) - 1] = i - 1
                    player_1_crowns.append(i - 1)
                    player_2_pawns.append(i)
                    sequence_of_moves.append("p1Sp2P: " + str(i) + "<->" + str(i - 1))
                    action = 1
                elif (((i - 1) in player_2_crowns) and sequence_of_moves[-1] != ("p1Sp2P: " + str(i - 1) + "<->" + str(i))):
                    player_1_crowns.remove(i)
                    All_Numbers[i - 1] = i
                    player_2_crowns.remove(i - 1)
                    All_Numbers[(i - 1) - 1] = i - 1
                    player_1_crowns.append(i - 1)
                    player_2_crowns.append(i)
                    sequence_of_moves.append("p1Sp2C: " + str(i) + "<->" + str(i - 1))
                    action = 1
            else:
                    print("Some case not considered in swap")
                    action = 0
        else:  # player doesn't have any viable crowns to use to swap
            action = 0
    else:
        print("player_1 doesn't have any crowns")
        action = 0

    return (All_Numbers, player_1_pawns, player_1_crowns, player_2_pawns, player_2_crowns
            , sequence_of_moves, action)

def promoteplayer1spawns(player_1_pawns, player_1_crowns, player_2_pawns, player_2_crowns
                            , sequence_of_moves,All_Numbers):
    possible_promotions = []
    for i in player_1_pawns:
        if ((i in player_1_pawns) and
                (i - 1 in player_1_pawns) and
                (i - 2 in player_1_pawns)):
            possible_promotions.append([i - 2, i, i - 1])
        elif ((i in player_1_pawns) and
              (i - 1 in player_1_pawns) and
              (i + 1 in player_1_pawns)):
            possible_promotions.append([i - 1, i, i + 1])
        elif ((i in player_1_pawns) and
              (i + 1 in player_1_pawns) and
              (i + 2 in player_1_pawns)):
            possible_promotions.append([i + 1, i, i + 2])
        elif ((i in player_1_pawns) and
              (i - 14 in player_1_pawns) and
              (i - 7 in player_1_pawns)):
            possible_promotions.append([i - 14, i, i - 7])
        elif ((i in player_1_pawns) and
              (i - 7 in player_1_pawns) and
              (i + 7 in player_1_pawns)):
            possible_promotions.append([i - 7, i, i + 7])
        elif ((i in player_1_pawns) and
              (i + 7 in player_1_pawns) and
              (i + 14 in player_1_pawns)):
            possible_promotions.append([i + 7, i, i + 14])

    if (len(possible_promotions) >= 1):
        r6 = np.random.randint(0, len(possible_promotions), 1)
        print("Possible Promotions: " + str(possible_promotions))
        selected_triple_for_promotion = possible_promotions[r6[0]]
        print("Selected triple for promotion: " + str(selected_triple_for_promotion))
        print("Player 1 Pawns and Crowns" + str(player_1_pawns)
              + str(player_1_crowns))

        for i in selected_triple_for_promotion:
            player_1_pawns.remove(i)
            ######### add regular number back to board
            All_Numbers[i - 1] = i


        q = np.mean(selected_triple_for_promotion)
        player_1_crowns.append(int(q))
        sequence_of_moves.append("p2Pp1: " + str(np.mean(selected_triple_for_promotion)))
        action = 1
        print("$$$$$$$$$$$$$$$$$$")
        print("$$$$$$$$$$$$$$$$$$")

    else:
        print("None of player 1's pawns can be promoted")
        action = 0

    return (player_1_pawns, player_1_crowns, player_2_pawns,
            player_2_crowns, sequence_of_moves, action,All_Numbers)

def player2swaps(All_Numbers, player_1_pawns, player_1_crowns, player_2_pawns, player_2_crowns
                 , sequence_of_moves):
    reasonable_swap_player_2_crowns = []
    action = 0

    if (len(player_2_crowns) >= 1):
        for i in player_2_crowns:
            if (((i - 7) in (player_1_pawns + player_1_crowns)) and ((i - 7) in [2, 3, 4, 5, 6])) or (
                    ((i + 1) in (player_1_pawns + player_1_crowns)) and ((i + 1) in [14, 21, 28, 35, 42])) or (
                    ((i + 7) in (player_1_pawns + player_1_crowns)) and ((i + 7) in [44, 45, 46, 47, 48])) or (
                    ((i - 1) in (player_1_pawns + player_1_crowns)) and ((i - 1) in [8, 15, 22, 29, 36])):
                reasonable_swap_player_2_crowns.append(i)

        if (len(reasonable_swap_player_2_crowns) >= 1):
            r7 = np.random.randint(0, len(reasonable_swap_player_2_crowns), 1)
            player_2_crown_selected = reasonable_swap_player_2_crowns[r7[0]]
            i = player_2_crown_selected
            #action = 1  ##strange place to put this

            if (((i - 7) in (player_1_pawns + player_1_crowns)) and (
                    (i - 7) in [2, 3, 4, 5, 6])):  ###doesn't consider bottom/horiz of cross
                if (((i - 7) in player_1_pawns) and sequence_of_moves[-1] != ("p2Sp1P: " + str(i - 7) + "<->" + str(i))):
                    player_2_crowns.remove(i)
                    print(i)
                    All_Numbers[i - 1] = i
                    player_1_pawns.remove(i - 7)
                    All_Numbers[(i - 7) - 1] = i - 7
                    player_2_crowns.append(i - 7)
                    player_1_pawns.append(i)
                    sequence_of_moves.append("p2Sp1P: " + str(i) + "<->" + str(i - 7))
                    action = 1
                elif (((i - 7) in player_2_crowns) and sequence_of_moves[-1] != ("p1Sp2C: " + str(i - 7) + "<->" + str(i))):
                    player_2_crowns.remove(i)
                    All_Numbers[i - 1] = i
                    player_1_crowns.remove(i - 7)
                    All_Numbers[(i - 7) - 1] = i - 7
                    player_2_crowns.append(i - 7)
                    player_1_crowns.append(i)
                    sequence_of_moves.append("p2Sp1C: " + str(i) + "<->" + str(i - 7))
                    action = 1
            elif (((i + 1) in (player_1_pawns + player_1_crowns)) and ((i + 1) in [14, 21, 28, 35, 42])):
                if (((i + 1) in player_1_pawns) and sequence_of_moves[-1] != ("p2Sp1P: " + str(i + 1) + "<->" + str(i))):
                    player_2_crowns.remove(i)
                    All_Numbers[i - 1] = i
                    player_1_pawns.remove(i + 1)
                    All_Numbers[(i + 1) - 1] = i + 1
                    player_2_crowns.append(i + 1)
                    player_1_pawns.append(i)
                    sequence_of_moves.append("p2Sp1P: " + str(i) + "<->" + str(i + 1))
                    action = 1
                elif (((i + 1) in player_1_crowns) and sequence_of_moves[-1] != ("p2Sp1C: " + str(i + 1) + "<->" + str(i))):
                    player_2_crowns.remove(i)
                    All_Numbers[i - 1] = i
                    player_1_crowns.remove(i + 1)
                    All_Numbers[(i + 1) - 1] = i + 1
                    player_2_crowns.append(i + 1)
                    player_1_crowns.append(i)
                    sequence_of_moves.append("p2Sp1C: " + str(i) + "<->" + str(i + 1))
                    action = 1
            elif (((i + 7) in (player_1_pawns + player_1_crowns)) and (
                            (i + 7) in [44, 45, 46, 47, 48])):
                if (((i + 7) in player_1_pawns) and sequence_of_moves[-1] != ("p2Sp1P: " + str(i + 7) + "<->" + str(i))):
                    player_2_crowns.remove(i)
                    All_Numbers[i - 1] = i
                    player_1_pawns.remove(i + 7)
                    All_Numbers[(i + 7) - 1] = i + 7
                    player_2_crowns.append(i + 7)
                    player_1_pawns.append(i)
                    sequence_of_moves.append("p2Sp1P: " + str(i) + "<->" + str(i + 7))
                    action = 1
                elif (((i + 7) in player_1_crowns) and sequence_of_moves[-1] != ("p2Sp1C: " + str(i + 7) + "<->" + str(i))):
                    player_2_crowns.remove(i)
                    All_Numbers[i - 1] = i
                    player_1_crowns.remove(i + 7)
                    All_Numbers[(i + 7) - 1] = i + 7
                    player_2_crowns.append(i + 7)
                    player_1_crowns.append(i)
                    sequence_of_moves.append("p2Sp1C: " + str(i) + "<->" + str(i + 7))
                    action = 1
            elif (((i - 1) in (player_1_pawns + player_1_crowns)) and ((i - 1) in [8, 15, 22, 29, 36])):
                if (((i - 1) in player_1_pawns) and sequence_of_moves[-1] != ("p2Sp1P: " + str(i - 1) + "<->" + str(i))):
                    player_2_crowns.remove(i)
                    All_Numbers[i - 1] = i
                    player_1_pawns.remove(i - 1)
                    All_Numbers[(i - 1) - 1] = i - 1
                    player_2_crowns.append(i - 1)
                    player_1_pawns.append(i)
                    sequence_of_moves.append("p2Sp1P: " + str(i) + "<->" + str(i - 1))
                    action = 1
                elif (((i - 1) in player_1_crowns) and sequence_of_moves[-1] != ("p2Sp1P: " + str(i - 1) + "<->" + str(i))):
                    player_2_crowns.remove(i)
                    All_Numbers[i - 1] = i
                    player_1_crowns.remove(i - 1)
                    All_Numbers[(i - 1) - 1] = i - 1
                    player_2_crowns.append(i - 1)
                    player_1_crowns.append(i)
                    sequence_of_moves.append("p2Sp1C: " + str(i) + "<->" + str(i - 1))
                    action = 1
            else:
                    print("Some case not considered in swap")
                    action = 0
        else:  # player doesn't have any viable crowns to use to swap
            action = 0
    else:
        print("player_2 doesn't have any crowns")
        action = 0

    return (All_Numbers, player_1_pawns, player_1_crowns, player_2_pawns, player_2_crowns
            , sequence_of_moves, action)

def canplayer1spawn(player_1_pawns,player_1_crowns,player_2_pawns,player_2_crowns,sequence_of_moves):

    available_spawn_nodes_p1 = [9,41]
    spawn_nodes_to_remove_p1 = []

    for i in (player_1_pawns + player_1_crowns + player_2_pawns + player_2_crowns):
        if ((i == 9) or (i == 41)):
            spawn_nodes_to_remove_p1.append(i)

    if len(spawn_nodes_to_remove_p1) >= 1:
        print("length of spawn nodes to remove: " + str(len(spawn_nodes_to_remove_p1)))
        print(available_spawn_nodes_p1)
        for j in spawn_nodes_to_remove_p1:
            #print("J: " + str(j))
            #print(available_spawn_nodes_p1)
            #print("Spawn: " + str(spawn_nodes_to_remove_p1))
            available_spawn_nodes_p1.remove(j)
            #print(available_spawn_nodes_p1)
            #print("========")

    print("Spawn Nodes to remove from player 1: " + str(spawn_nodes_to_remove_p1))
    print("Available spawn nodes for player 1: " + str(available_spawn_nodes_p1))

    if len(available_spawn_nodes_p1) >= 1: #if there is at least one spawn available to spawn from
        r2 = np.random.randint(0,len(available_spawn_nodes_p1),1)
        player_1_selected_spawn_node = available_spawn_nodes_p1[r2[0]]
        print("Player 1 selected spawn node: " + str(player_1_selected_spawn_node))
        player_1_pawns.append(player_1_selected_spawn_node)
        sequence_of_moves.append("p1s: " + str(player_1_selected_spawn_node))
        spawned = 1
    else:
        spawned = 0

    return (player_1_pawns,player_1_crowns,player_2_pawns,player_2_crowns,sequence_of_moves,spawned)

def canplayer2spawn(player_1_pawns,player_1_crowns,player_2_pawns,player_2_crowns,sequence_of_moves):

    available_spawn_nodes_p2 = [13,37]
    spawn_nodes_to_remove_p2 = []

    for i in (player_1_pawns + player_1_crowns + player_2_pawns + player_2_crowns):
        if ((i == 13) or (i == 37)):
            spawn_nodes_to_remove_p2.append(i)

    if len(spawn_nodes_to_remove_p2) >= 1:
        print("length of spawn nodes to remove: " + str(len(spawn_nodes_to_remove_p2)))
        print(available_spawn_nodes_p2)
        for j in spawn_nodes_to_remove_p2:
            #print("J: " + str(j))
            #print(available_spawn_nodes_p1)
            #print("Spawn: " + str(spawn_nodes_to_remove_p1))
            available_spawn_nodes_p2.remove(j)
            #print(available_spawn_nodes_p1)
            #print("========")

    print("Spawn Nodes to remove from player 2: " + str(spawn_nodes_to_remove_p2))
    print("Available spawn nodes for player 2: " + str(available_spawn_nodes_p2))

    if len(available_spawn_nodes_p2) >= 1: #if there is at least one spawn available to spawn from
        r2 = np.random.randint(0,len(available_spawn_nodes_p2),1)
        player_2_selected_spawn_node = available_spawn_nodes_p2[r2[0]]
        print("Player 2 selected spawn node: " + str(player_2_selected_spawn_node))
        player_2_pawns.append(player_2_selected_spawn_node)
        sequence_of_moves.append("p2s: " + str(player_2_selected_spawn_node))
        spawned = 1
    else:
        spawned = 0

    return (player_1_pawns,player_1_crowns,player_2_pawns,player_2_crowns,sequence_of_moves,spawned)

def checkvictory(player_1_pawns, player_1_crowns, player_2_pawns, player_2_crowns,action):
    Cross = {11, 18, 25, 32, 39, 23, 24, 26, 27}
    Cross1 = [11, 18, 25, 32, 39, 23, 24, 26, 27]
    A = {2, 3, 4, 5, 6}
    B = {44, 45, 46, 47, 48}
    C = {8, 15, 22, 29, 36}
    D = {14, 21, 28, 35, 42}

    player_1_pawns_set = set(player_1_pawns)
    player_1_crowns_set = set(player_1_crowns)
    player_2_pawns_set = set(player_2_pawns)
    player_2_crowns_set = set(player_2_crowns)

    player_1_cross = []
    player_2_cross = []

    player_1_win = 0
    player_2_win = 0
    terminate = 0
    ####### Check A-D
    if ((A.issubset(player_1_pawns_set.union(player_1_crowns_set))) == True):
        print("Player 1 possesses top numbers")
        player_1_win = 1
        terminate = 1
        action = 3
    elif ((B.issubset(player_1_pawns_set.union(player_1_crowns_set))) == True):
        print("Player 1 possesses bottom numbers")
        player_1_win = 1
        terminate = 1
        action = 3

    elif ((C.issubset(player_1_pawns_set.union(player_1_crowns_set))) == True):
        print("Player 1 possesses left numbers")
        player_1_win = 1
        terminate = 1
        action = 3

    elif ((D.issubset(player_1_pawns_set.union(player_1_crowns_set))) == True):
        print("Player 1 possesses right numbers")
        player_1_win = 1
        terminate = 1
        action = 3

    #######################################################
    elif ((A.issubset(player_2_pawns_set.union(player_2_crowns_set))) == True):
        print("Player 2 possesses top numbers")
        player_2_win = 1
        terminate = 1
        action = 3

    elif ((B.issubset(player_2_pawns_set.union(player_2_crowns_set))) == True):
        print("Player 2 possesses bottom numbers")
        player_2_win = 1
        terminate = 1
        action = 3

    elif ((C.issubset(player_2_pawns_set.union(player_2_crowns_set))) == True):
        print("Player 2 possesses left numbers")
        player_2_win = 1
        terminate = 1
        action = 3

    elif ((D.issubset(player_2_pawns_set.union(player_2_crowns_set))) == True):
        print("Player 2 possesses right numbers")
        player_2_win = 1
        terminate = 1
        action = 3

    ########################################################
    elif Cross.issubset(
            player_1_pawns_set.union(player_1_crowns_set.union(player_2_pawns_set.union(player_2_crowns_set)))):
        print("The Cross is filled.")
        for n in Cross1:
            if n in (player_1_pawns_set.union(player_1_crowns_set)):
                player_1_cross.append(n)
            elif n in (player_2_pawns_set.union(player_2_pawns_set)):
                player_2_cross.append(n)
        if (len(player_1_cross) > len(player_2_cross)):
            player_1_win = 1
            terminate = 1
            action = 3

        elif (len(player_1_cross) < len(player_2_cross)):
            player_2_win = 1
            terminate = 1
            action = 3

        else:
            print("Cross Tie: Error occurred in Victory")
            terminate = 0

    return (player_1_win, player_2_win, terminate, action)

Total_Player_1_wins = 0
Total_Player_2_wins = 0
Total_Sequences = []
Total_Length_of_Sequences = []
Sequence_player_1_wins = []
Sequence_player_2_wins = []

number_of_games = 1
game = 0

while game < number_of_games:
    player_1_win = 0
    player_2_win = 0
    #############################################

    All_Numbers = [1,2,3,4,5,6,7,
                8,9,10,11,12,13,14,
                15,16,17,18,19,20,21,
                22,23,24,25,26,27,28,
                29,30,31,32,33,34,35,
                36,37,38,39,40,41,42,
                43,44,45,46,47,48,49]

    ############initial placement
    player_1_pawns = [9,41]
    player_1_crowns = []
    player_2_pawns = [13,37]
    player_2_crowns = []
    ### note: may need to add a clause restricting player sets


    print("Initial Placement: ")
    print("")
    playerboard(All_Numbers, player_1_pawns, player_1_crowns, player_2_pawns, player_2_crowns)
    print("------------------------------------------------------------")
    print("------------------------------------------------------------")
    print("------------------------------------------------------------")

    sequence_of_moves = []

    ########################## Begin Initial Turn ############################
    action = 0

    while action < 3:
        Player1MoveAction = player_1_moveaction(All_Numbers, player_1_pawns, player_1_crowns,
                            player_2_pawns, player_2_crowns, sequence_of_moves)
        All_Numbers = Player1MoveAction[0]
        player_1_pawns = Player1MoveAction[1]
        player_1_crowns = Player1MoveAction[2]
        player_2_pawns = Player1MoveAction[3]
        player_2_crowns = Player1MoveAction[4]
        sequence_of_moves = Player1MoveAction[5]
        actionfromplayer1move = Player1MoveAction[6]


        playerboard(All_Numbers, player_1_pawns, player_1_crowns, player_2_pawns, player_2_crowns)
        print("Action number: " + str(action + 1))
        print("")
        print("")
        action = action + actionfromplayer1move

    ################################ begin player 2 initial turn
    print("")
    print("*************************************")
    print("Begin player 2 turn")
    print("*************************************")
    print("")
    action = 0

    while action < 3:
        Player2MoveAction = player_2_moveaction(All_Numbers, player_1_pawns, player_1_crowns,
                            player_2_pawns, player_2_crowns, sequence_of_moves)
        All_Numbers = Player2MoveAction[0]
        player_1_pawns = Player2MoveAction[1]
        player_1_crowns = Player2MoveAction[2]
        player_2_pawns = Player2MoveAction[3]
        player_2_crowns = Player2MoveAction[4]
        sequence_of_moves = Player2MoveAction[5]


        playerboard(All_Numbers, player_1_pawns, player_1_crowns, player_2_pawns, player_2_crowns)
        print("Action number: " + str(action + 1))
        print("")
        print("")
        action = action + 1

    ###############################################
    ########################## Begin Turn 2: ############################
    ###while player1victory or player2victory is not met  ---> i.e. neither player contains ....
    ##check player 1 spawns, if either is available,flip a coin, then spawn a node place into playerpawn,
    # else, if
    # select one of the..
    ##..then
    ##### roll dice ---> 1,2, or 3, if 1 then select a piece and if move--use the above
    terminate = 0

    while ((terminate != 1)):

        Check_Victory = checkvictory(player_1_pawns, player_1_crowns, player_2_pawns, player_2_crowns,action)
        player_1_win = Check_Victory[0]
        player_2_win = Check_Victory[1]
        terminate = Check_Victory[2]
        action = Check_Victory[3]

        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        print("Begin Turn 2")

        ############ check if player 1 can spawn a node

        Can_Player_1_Spawn = canplayer1spawn(player_1_pawns,player_1_crowns,player_2_pawns,player_2_crowns,sequence_of_moves)
        player_1_pawns = Can_Player_1_Spawn[0]
        player_1_crowns = Can_Player_1_Spawn[1]
        player_2_pawns = Can_Player_1_Spawn[2]
        player_2_crowns = Can_Player_1_Spawn[3]
        sequence_of_moves = Can_Player_1_Spawn[4]
        spawned = Can_Player_1_Spawn[5]

        ################################

        action = 0

        ######## if no spawn of node, then required first move

        if spawned == 0:  #there aren't any open spawns to spawn from, so player must try to move if they contain one of 9 or 41
            print("Player 1 could not spawn.")
            possible_player_1_occupied_spawnnodes = []
            for i in (player_1_pawns+player_1_crowns+player_2_pawns+player_2_crowns):
                if (i == 9 or i == 41):
                    if (i == 9 and (i in player_1_pawns or i in player_1_crowns)):
                        possible_player_1_occupied_spawnnodes.append(i)
                    elif (i == 41 and (i in player_1_pawns or i in player_1_crowns)):
                        possible_player_1_occupied_spawnnodes.append(i)
                    else:
                        print("Neither 9 nor 41 is part of Player 1's union of pawns and crowns.")
                    ##########can add case of manipulating player 2's nodes

            if len(possible_player_1_occupied_spawnnodes) > 0: #if player possesses at least one of the spawn nodes

                player_1_pawn_or_crown_selected_for_move = 0
                pseudovar_player_1_pawns_and_crowns = possible_player_1_occupied_spawnnodes

                while player_1_pawn_or_crown_selected_for_move < 1:

                    r3 = np.random.randint(0, len(pseudovar_player_1_pawns_and_crowns), 1)
                    player_1_selected_spawnnode_to_move = possible_player_1_occupied_spawnnodes[r3[0]]
                    player_1_selected_node = player_1_selected_spawnnode_to_move
                    print("Player 1 selected pawn/crown on spawn node: " + str(player_1_selected_spawnnode_to_move))

                    ######### Check possible moves for player 1 selected node#####
                    check_possible_moves_p1 = checkpossiblemoves_p1(player_1_selected_node,
                                                                    player_1_pawns + player_1_crowns,
                                                                    player_2_pawns + player_2_crowns,
                                                                    sequence_of_moves)

                    complete_move_options = check_possible_moves_p1
                    if len(complete_move_options) > 0:

                        ###### might be wrong ############

                        ############ randomly picking a move direction
                        r2 = np.random.randint(0, len(complete_move_options), 1)
                        move_chosen = complete_move_options[r2[0]]  # ex. =2, from 9

                        ####### remove number from pawn or crown from set
                        for i in (player_1_pawns):  # looking at all numbers in player's pawn set
                            if (i == player_1_selected_node):
                                player_1_pawns.remove(i)
                                player_1_pawns.append(move_chosen)
                                ######### add regular number back to board
                                All_Numbers[i - 1] = player_1_selected_node

                        for i in (player_1_crowns):  # looking at all numbers in player's crown set
                            if (i == player_1_selected_node):
                                player_1_crowns.remove(i)
                                player_1_crowns.append(move_chosen)
                                ######### add regular number back to board
                                All_Numbers[i - 1] = player_1_selected_node

                        sequence_of_moves.append("p1: " + str(player_1_selected_node) + "->" + str(move_chosen))
                        action = action + 1  ##added if the player moves off spawn node
                        ###############################################
                        player_1_pawn_or_crown_selected_for_move = 1

                        ##################################

                    else:
                        player_1_pawn_or_crown_selected_for_move = 0
                        pseudovar_player_1_pawns_and_crowns.remove(player_1_selected_node)
                        if len(pseudovar_player_1_pawns_and_crowns) == 0:
                            print("Neither occupied spawn node (player possession) can be moved.")
                            break

            else: #############can add clause trying to swap or condense opponents pieces surrounding, current case
                ############## player doesn't have any spawn nodes
                print("The player doesn't possess either of their spawn nodes.")
                ############ try to move, promote, or swap

        Check_Victory = checkvictory(player_1_pawns, player_1_crowns, player_2_pawns, player_2_crowns,action)
        player_1_win = Check_Victory[0]
        player_2_win = Check_Victory[1]
        terminate = Check_Victory[2]
        action = Check_Victory[3]

        #################end of required first move

        non_available_action = []
        while action < 3:
            Check_Victory = checkvictory(player_1_pawns, player_1_crowns, player_2_pawns, player_2_crowns,action)
            player_1_win = Check_Victory[0]
            player_2_win = Check_Victory[1]
            terminate = Check_Victory[2]
            action = Check_Victory[3]

            ###initial check if action unavailable
            if ((0 in non_available_action) and (1 in non_available_action)
                    and (2 in non_available_action)):
                print("There are no available actions for Player 1 to make!!! ")
                break
            ########choose an action 0=move, 1=promote, 2=swap
            r5 = np.random.randint(0,3,1)
            print("")
            print("")
            print("Action Choosen: " + str(r5[0]))
            if r5[0] == 0:
                ## attempt to perform a move
                Player1MoveAction = player_1_moveaction(All_Numbers, player_1_pawns, player_1_crowns,
                                                        player_2_pawns, player_2_crowns, sequence_of_moves)
                All_Numbers = Player1MoveAction[0]
                player_1_pawns = Player1MoveAction[1]
                player_1_crowns = Player1MoveAction[2]
                player_2_pawns = Player1MoveAction[3]
                player_2_crowns = Player1MoveAction[4]
                sequence_of_moves = Player1MoveAction[5]
                actionfromplayer1move = Player1MoveAction[6]

                #playerboard(All_Numbers, player_1_pawns, player_1_crowns, player_2_pawns, player_2_crowns)
                #print("Action number: " + str(action + 1))
                #print("")
                #print("")

                if actionfromplayer1move == 0:
                    print("Player 1 cannot move.")
                    non_available_action.append(0)

                if action != (action + actionfromplayer1move): ## the action works
                        non_available_action = []
                        ##resets this to ensure that a unavailable move from prior isn't taken into account

                action = action + actionfromplayer1move
                print("))))))))))))))")


            elif r5[0] == 1:
                print("Promote function")
                print("")
                Promote_Player_2s_Pawns = promoteplayer2spawns(player_1_pawns, player_1_crowns, player_2_pawns, player_2_crowns
                                        , sequence_of_moves,All_Numbers)
                player_1_pawns = Promote_Player_2s_Pawns[0]
                player_1_crowns = Promote_Player_2s_Pawns[1]
                player_2_pawns = Promote_Player_2s_Pawns[2]
                player_2_crowns = Promote_Player_2s_Pawns[3]
                print("Player 2 pawns after promoting: " + str(player_2_pawns))
                print("Player 2 crowns after promoting: " + str(player_2_crowns))
                sequence_of_moves = Promote_Player_2s_Pawns[4]
                actionpromote = Promote_Player_2s_Pawns[5]
                All_Numbers = Promote_Player_2s_Pawns[6]

                if actionpromote == 0:
                    print("Player 1 cannot promote any of Player 2's pawns.")
                    non_available_action.append(1)

                if action != (action + actionpromote): ## the action works
                        non_available_action = []
                        ##resets this to ensure that a unavailable move from prior isn't taken into account

                action = action + actionpromote
                print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%5")
                print("")



            elif r5[0] == 2:
                print("Swap function: ")

                Player_1_Swaps = player1swaps(All_Numbers, player_1_pawns, player_1_crowns, player_2_pawns,
                                              player_2_crowns, sequence_of_moves)
                All_Numbers = Player_1_Swaps[0]
                player_1_pawns = Player_1_Swaps[1]
                player_1_crowns = Player_1_Swaps[2]
                player_2_pawns = Player_1_Swaps[3]
                player_2_crowns = Player_1_Swaps[4]
                sequence_of_moves = Player_1_Swaps[5]
                actionswap = Player_1_Swaps[6]

                if actionswap == 0:
                    print("Player 1 cannot swap.")
                    non_available_action.append(2)

                if action != (action + actionswap): ## the action works
                        non_available_action = []
                        ##resets this to ensure that a unavailable move from prior isn't taken into account

                action = action + actionswap



            else:
                print("Case not considered in picking one of three options for player 1")



            Check_Victory = checkvictory(player_1_pawns, player_1_crowns, player_2_pawns, player_2_crowns,action)
            player_1_win = Check_Victory[0]
            player_2_win = Check_Victory[1]
            terminate = Check_Victory[2]
            action = Check_Victory[3]

            print("Playerboard")
            playerboard(All_Numbers, player_1_pawns, player_1_crowns, player_2_pawns, player_2_crowns)
            print("Playerboard")
            print("")





        print("Sequence of Moves: " + textwrap.fill(str(sequence_of_moves), 30))


        ##########################################################################################################


        ############ check if player 2 can spawn a node

        Can_Player_2_Spawn = canplayer2spawn(player_1_pawns,player_1_crowns,player_2_pawns,player_2_crowns,sequence_of_moves)
        player_1_pawns = Can_Player_2_Spawn[0]
        player_1_crowns = Can_Player_2_Spawn[1]
        player_2_pawns = Can_Player_2_Spawn[2]
        player_2_crowns = Can_Player_2_Spawn[3]
        sequence_of_moves = Can_Player_2_Spawn[4]
        spawned = Can_Player_2_Spawn[5]

        ################################

        action = 0

        Check_Victory = checkvictory(player_1_pawns, player_1_crowns, player_2_pawns, player_2_crowns,action)
        player_1_win = Check_Victory[0]
        player_2_win = Check_Victory[1]
        terminate = Check_Victory[2]
        action = Check_Victory[3]


        ######## if no spawn of node, then required first move

        if spawned == 0:  #there aren't any open spawns to spawn from, so player must try to move if they contain one of 9 or 41
            print("Player 2 could not spawn.")
            possible_player_2_occupied_spawnnodes = []
            for i in (player_1_pawns+player_1_crowns+player_2_pawns+player_2_crowns):
                if (i == 13 or i == 37):
                    if (i == 13 and (i in player_2_pawns or i in player_2_crowns)):
                        possible_player_2_occupied_spawnnodes.append(i)
                    elif (i == 37 and (i in player_2_pawns or i in player_2_crowns)):
                        possible_player_2_occupied_spawnnodes.append(i)
                    else:
                        print("Neither 13 nor 37 is part of Player 2's union of pawns and crowns.")
                    ##########can add case of manipulating player 2's nodes

            if len(possible_player_2_occupied_spawnnodes) > 0: #if player possesses at least one of the spawn nodes

                player_2_pawn_or_crown_selected_for_move = 0
                pseudovar_player_2_pawns_and_crowns = possible_player_2_occupied_spawnnodes

                while player_2_pawn_or_crown_selected_for_move < 1:

                    r3 = np.random.randint(0, len(pseudovar_player_2_pawns_and_crowns), 1)
                    player_2_selected_spawnnode_to_move = possible_player_2_occupied_spawnnodes[r3[0]]
                    player_2_selected_node = player_2_selected_spawnnode_to_move
                    print("Player 2 selected pawn/crown on spawn node: " + str(player_2_selected_spawnnode_to_move))

                    ######### Check possible moves for player 1 selected node#####
                    check_possible_moves_p2 = checkpossiblemoves_p2(player_2_selected_node,
                                                                    player_1_pawns + player_1_crowns,
                                                                    player_2_pawns + player_2_crowns,
                                                                    sequence_of_moves)

                    complete_move_options = check_possible_moves_p2
                    if len(complete_move_options) > 0:

                        ###### might be wrong ############

                        ############ randomly picking a move direction
                        r2 = np.random.randint(0, len(complete_move_options), 1)
                        move_chosen = complete_move_options[r2[0]]  # ex. =2, from 9

                        ####### remove number from pawn or crown from set
                        for i in (player_2_pawns):  # looking at all numbers in player's pawn set
                            if (i == player_2_selected_node):
                                player_2_pawns.remove(i)
                                player_2_pawns.append(move_chosen)
                                ######### add regular number back to board
                                All_Numbers[i - 1] = player_2_selected_node

                        for i in (player_2_crowns):  # looking at all numbers in player's crown set
                            if (i == player_2_selected_node):
                                player_2_crowns.remove(i)
                                player_2_crowns.append(move_chosen)
                                ######### add regular number back to board
                                All_Numbers[i - 1] = player_2_selected_node

                        sequence_of_moves.append("p2: " + str(player_2_selected_node) + "->" + str(move_chosen))
                        action = action + 1  ##added if the player moves off spawn node
                        ###############################################
                        player_2_pawn_or_crown_selected_for_move = 1

                        ##################################

                    else:
                        player_2_pawn_or_crown_selected_for_move = 0
                        pseudovar_player_2_pawns_and_crowns.remove(player_2_selected_node)
                        if len(pseudovar_player_2_pawns_and_crowns) == 0:
                            print("Neither occupied spawn node (player possession) can be moved.")
                            break

            else: #############can add clause trying to swap or condense opponents pieces surrounding, current case
                ############## player doesn't have any spawn nodes
                print("The player doesn't possess either of their spawn nodes.")
                ############ try to move, promote, or swap

        #################end of required first move

        non_available_action = []
        while action < 3:

            Check_Victory = checkvictory(player_1_pawns, player_1_crowns, player_2_pawns, player_2_crowns,action)
            player_1_win = Check_Victory[0]
            player_2_win = Check_Victory[1]
            terminate = Check_Victory[2]
            action = Check_Victory[3]

            ###initial check if action unavailable
            if ((0 in non_available_action) and (1 in non_available_action)
                    and (2 in non_available_action)):
                print("There are no available actions for Player 2 to make!!! ")
                break
            ########choose an action 0=move, 1=promote, 2=swap
            r5 = np.random.randint(0,3,1)
            print("")
            print("")
            print("Action Choosen: " + str(r5[0]))
            if r5[0] == 0:
                ## attempt to perform a move
                Player2MoveAction = player_2_moveaction(All_Numbers, player_1_pawns, player_1_crowns,
                                                        player_2_pawns, player_2_crowns, sequence_of_moves)
                All_Numbers = Player2MoveAction[0]
                player_1_pawns = Player2MoveAction[1]
                player_1_crowns = Player2MoveAction[2]
                player_2_pawns = Player2MoveAction[3]
                player_2_crowns = Player2MoveAction[4]
                sequence_of_moves = Player2MoveAction[5]
                actionfromplayer2move = Player2MoveAction[6]

                #playerboard(All_Numbers, player_1_pawns, player_1_crowns, player_2_pawns, player_2_crowns)
                #print("Action number: " + str(action + 1))
                #print("")
                #print("")

                if actionfromplayer2move == 0:
                    print("Player 2 cannot move.")
                    non_available_action.append(0)

                if action != (action + actionfromplayer2move): ## the action works
                        non_available_action = []
                        ##resets this to ensure that a unavailable move from prior isn't taken into account

                action = action + actionfromplayer2move
                print("))))))))))))))")


            elif r5[0] == 1:
                print("Promote function")
                print("")
                Promote_Player_1s_Pawns = promoteplayer1spawns(player_1_pawns, player_1_crowns, player_2_pawns, player_2_crowns
                                        , sequence_of_moves,All_Numbers)
                player_1_pawns = Promote_Player_1s_Pawns[0]
                player_1_crowns = Promote_Player_1s_Pawns[1]
                player_2_pawns = Promote_Player_1s_Pawns[2]
                player_2_crowns = Promote_Player_1s_Pawns[3]
                print("Player 1 pawns after promoting: " + str(player_1_pawns))
                print("Player 1 crowns after promoting: " + str(player_1_crowns))
                sequence_of_moves = Promote_Player_1s_Pawns[4]
                actionpromote = Promote_Player_1s_Pawns[5]
                All_Numbers = Promote_Player_1s_Pawns[6]

                if actionpromote == 0:
                    print("Player 2 cannot promote any of Player 1's pawns.")
                    non_available_action.append(1)

                if action != (action + actionpromote): ## the action works
                        non_available_action = []
                        ##resets this to ensure that a unavailable move from prior isn't taken into account

                action = action + actionpromote
                print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%5")
                print("")


            elif r5[0] == 2:
                print("Swap function: ")

                Player_2_Swaps = player2swaps(All_Numbers, player_1_pawns, player_1_crowns, player_2_pawns,
                                              player_2_crowns, sequence_of_moves)
                All_Numbers = Player_2_Swaps[0]
                player_1_pawns = Player_2_Swaps[1]
                player_1_crowns = Player_2_Swaps[2]
                player_2_pawns = Player_2_Swaps[3]
                player_2_crowns = Player_2_Swaps[4]
                sequence_of_moves = Player_2_Swaps[5]
                actionswap = Player_2_Swaps[6]

                if actionswap == 0:
                    print("Player 2 cannot swap.")
                    non_available_action.append(2)

                if action != (action + actionswap): ## the action works
                        non_available_action = []
                        ##resets this to ensure that a unavailable move from prior isn't taken into account

                action = action + actionswap


            else:
                print("Case not considered in picking one of three options for player 2")

            Check_Victory = checkvictory(player_1_pawns, player_1_crowns, player_2_pawns, player_2_crowns,action)
            player_1_win = Check_Victory[0]
            player_2_win = Check_Victory[1]
            terminate = Check_Victory[2]
            action = Check_Victory[3]

            print("Playerboard")
            playerboard(All_Numbers, player_1_pawns, player_1_crowns, player_2_pawns, player_2_crowns)
            print("Playerboard")
            print("")



            if terminate == 1:
                print("Sequence of Moves: " + textwrap.fill(str(sequence_of_moves), 30))






    print("=============================================================")

    playerboard(All_Numbers, player_1_pawns, player_1_crowns, player_2_pawns, player_2_crowns)

    print("Player 1 Won: " + str(player_1_win))
    print("Player 2 Won: " + str(player_2_win))
    print("Number of moves made(including spawns): " + str(len(sequence_of_moves)))
    print
    #print(player_1_pawns_and_crowns)
    print("Player 1 Pawns: " + str(player_1_pawns))
    print("Player 1 Crowns: " + str(player_1_crowns))
    print("Player 2 Pawns: " + str(player_2_pawns))
    print("Player 2 Crowns: " + str(player_2_crowns))





    Total_Player_1_wins = Total_Player_1_wins + player_1_win
    Total_Player_2_wins = Total_Player_2_wins + player_2_win
    Total_Sequences.append(sequence_of_moves)
    Total_Length_of_Sequences.append(len(sequence_of_moves))
    Sequence_player_1_wins.append(player_1_win)
    Sequence_player_2_wins.append(player_2_win)

    print("Total Games played: " + str(game+1))
    game = game + 1

print("ALLGAMESFINISHED-ALLGAMESFINISHED-ALLGAMESFINISHED-ALLGAMESFINISHED-ALLGAMESFINISHED")
print("")
print("")
minimum = min(Total_Length_of_Sequences)
minid = Total_Length_of_Sequences.index(minimum)
print("Total Player 1 wins: " + str(Total_Player_1_wins))
print("Total Player 2 wins: " + str(Total_Player_2_wins))
print("--------------------------------------------------")
print("Minimum Length of Sequence: " + str(minimum))
print("Player 1 Win min Sequence?: " + str(Sequence_player_1_wins[minid]))
print("Player 2 Win min Sequence?: " + str(Sequence_player_2_wins[minid]))
print("Sequence of Minimum Length: ")
print(textwrap.fill(str(Total_Sequences[minid]), 30))

print("Maximum Length of Sequence: " + str(max(Total_Length_of_Sequences)))
print("Lengths of Sequences: " + str(Total_Length_of_Sequences))

