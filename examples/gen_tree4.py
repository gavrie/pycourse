tree = ["chapter 1",
           ["section 1.1",
               ["paragraph 1.1.1",
                "paragraph 1.1.2",
                "paragraph 1.1.3",],
            "section 1.2",
               ["paragraph 1.2.1",]],
        "chapter 2",
           ["section 2.1",
               ["paragraph 2.1.1",
                "paragraph 2.1.2",],
            "section 2.2",],
        "chapter 3",
           ["section 3.1",
            "section 3.2",]]


def traverse_callback(tree, callback):

    def traverse(tree, level=0):
        if tree:
            for node in tree:
                if isinstance(node, basestring):
                    callback(node, level)
                else:
                    traverse(node, level = level + 1)

    traverse(tree)


def process_node(node, level):
    print "processing:", level, node

traverse_callback(tree, process_node)
