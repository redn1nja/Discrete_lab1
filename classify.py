from sklearn.datasets import load_iris
from functools import wraps
import numpy as np
iris = load_iris()

call_list = []
def trace(func):
    def traced_func(*args, **kwargs):
        result = func(*args, **kwargs)

        call_list.append(result)

        return result

    return traced_func


class Node:
    def __init__(self, X, y):  # тут ще було gini, забрав бо хз як в рекурсію нормаьно її додавати
        self.X = X
        self.y = y
        self.gini = 0  # self.gini = gini
        self.feature_index = 0
        self.threshold = 0
        self.left = None
        self.right = None
        self.depth = 0
        # self.leaf = False # додав атрибут з листками, тому що він грубо говоря, надо, хз що передавати в нього якщо чесно

    def __str__(self) -> str:
        return f"Node containing {len(self.X)} irises of type {np.unique(self.y)} @ depth {self.depth}"


class Leaf(Node):
    def __str__(self):
        return f"Leaf containing {len(self.X)} irises of type {np.unique(self.y)} @ depth {self.depth}"


class MyDecisionTreeClassifier:

    def __init__(self, max_depth):
        self.max_depth = max_depth  # height of a tree
        self.json_view = []

    def split_data(self, dataset):  # x -- dataset y -- target (0,1,2)
        # ця фція паше харашо, перебором но харашо, так і треба, можеш в принципі якщо щось якось розібратись.
        # test all the possible splits in O(N^2)S
        # return index and threshold value
        best_split = {}
        maximum = 1
        amount = np.shape(X)[1]
        for column in range(amount-1):
            values = X[:, column]
            possible_values = np.unique(values)
            for value in possible_values:
                left_tree = np.array(
                    [row for row in dataset if row[column] <= value])
                right_tree = np.array(
                    [row for row in dataset if row[column] > value])
                if left_tree.size != 0 and right_tree.size != 0:
                    y, y_left, y_right = dataset[:, -
                                                 1], left_tree[:, -1], right_tree[:, -1]
                    data = self.gini(y, y_left, y_right)
                    if data < maximum:
                        maximum = data
                        best_split['column'] = column
                        best_split['value'] = value
                        best_split['left_tree'] = left_tree
                        best_split['right_tree'] = right_tree
                        best_split['data'] = data
        return best_split

    # ця фція паше хорошо, просто обраховує велью за формулою, по якому ми потім визначаєм шо нам підходе

    def gini(self, y, left_y, right_y):
        '''
        A Gini score gives an idea of how good a split is by how mixed the
        classes are in the two groups created by the split.

        A perfect separation results in a Gini score of 0,
        whereas the worst case split that results in 50/50
        classes in each group result in a Gini score of 0.5
        (for a 2 class problem).
        '''
        left_w = len(left_y)/len(y)
        right_w = len(right_y)/len(y)
        gini = gini_left = gini_right = 1
        for num in np.unique(y):
            gini -= (len(y[y == num])/len(y))**2
        for num in np.unique(left_y):
            gini_left -= (len(left_y[left_y == num])/len(left_y))**2
        for num in np.unique(right_y):
            gini_right -= (len(right_y[right_y == num])/len(right_y))**2
        gain = gini-(left_w*gini_left + right_w*gini_right)
        return gain

    def build_tree(self, dataset, depth=0):  # гігантська рекурсія яка поки що (вже)
        # паше але чот ретурнить тільки нани, тому що треба бавитись з обжектами класу а я пока хз як тут зробити шоб воно пахало.
        # надіюсь в тебе вийде.
        # може треба подумати як створити корінь перед тим як рекурсивно ходити.

        # create a root node

        # recursively split until max depth is not exeeced

        # rows, columns = np.shape(X)
        # if depth < self.max_depth:
        left_tree = None
        right_tree = None
        split = self.split_data(dataset)
        if split:
            left_tree = self.build_tree(split['left_tree'], depth+1)
            right_tree = self.build_tree(split['right_tree'], depth+1)
            node = Node(dataset[:, :-1], dataset[:, -1])
            node.gini = split['data']
            node.feature_index = split['column']
            node.threshold = split['value']
            node.left = left_tree
            node.right = right_tree
            node.depth = depth
        else:
            node = Leaf(dataset[:, :-1], dataset[:, -1])
            node.depth = depth
        return node

    def fit(self, X, y):
        y = np.array([[i] for i in y])
        dataset = np.append(X, y, axis=1)
        np.random.shuffle(dataset)
        dataset = dataset[:-50]
        self.build_tree = trace(self.build_tree)
        nodes = self.build_tree(dataset)
        print("\n".join(str(node) for node in sorted(call_list, key=lambda x: int(str(x).split()[-1]))))
        return nodes



    # ходити по всім тресхолдам (split['value']) і перевіряти в яку гілку попадає новий елемент + повертати 0 1 чи 2 (тип квіки)
    def predict(self, X_test):

        # traverse the tree while there is left node
        # and return the predicted class for it,
        # note that X_test can be not only one example


        pass


if __name__ == '__main__':
    X = iris.data
    y = iris.target
    tree = MyDecisionTreeClassifier(100)
    nodes = tree.fit(X, y)
