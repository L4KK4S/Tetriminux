def score_new(score,nb_case):
    score += nb_case
    return score

def count_pt(block):
    """
            Give the score
            :param: block
            :type : list
            :return: score
            :rtype: int
            :Example:
                 >>> col_state([[1,0,0,1],[1,2,0,1],[1,2,2,1],[1,0,0,1]])
                   score=3
                        """
    score = 0
    for row in block:
        for cell in row:
            if cell == 2:
                score += 1
    return score

