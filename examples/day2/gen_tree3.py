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


def traverse_levels(tree, minlevel, maxlevel):

    def traverse(tree, level=1):
        if tree:
            for node in tree:
                if isinstance(node, basestring):
                    if minlevel <= level <= maxlevel:
                        print "   " * (level - minlevel), node
                else:
                    traverse(node, level = level + 1)

    traverse(tree)


traverse_levels(tree, 1, 1)
traverse_levels(tree, 2, 2)
traverse_levels(tree, 3, 3)
