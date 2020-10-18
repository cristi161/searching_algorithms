import math


def minimax(current_depth, node_index, max_turn, scores, target_depth):
    if current_depth == target_depth:
        return scores[node_index]
    print(scores)
    if max_turn:
        return max(minimax(current_depth + 1, node_index * 2, False, scores, target_depth),
                   minimax(current_depth + 1, node_index * 2 + 1, False, scores, target_depth))
    else:
        return min(minimax(current_depth + 1, node_index * 2, True, scores, target_depth),
                   minimax(current_depth + 1, node_index * 2 + 1, True, scores, target_depth))


scores = [3, 5, 2, 9, 12, 5, 23, 23]

treeDepth = math.log(len(scores), 2)

print("The optimal value is : ", end="")
print(minimax(0, 0, True, scores, treeDepth))

