'''
Created on 1 feb 2012

@author: anders
'''

def extractIndentationLevels(myObjects, indentDic):
    for layout in myObjects:
        if indentDic.has_key(layout.myid) != True:
            indentDic[layout.myid] = 0
        if layout.hasParent():
            if indentDic.has_key(layout.parentId) != True:
                indentDic[layout.parentId] = 0
            indentDic[layout.myid] += indentDic[layout.parentId] + 1


class Layout:
    def __init__(self, myid, parentId, childs = None):
        self.myid = myid
        self.parentId = parentId       
        self.childs = childs or []        
    
    def hasParent(self):        
        return self.myid != self.parentId

        
if __name__ == '__main__':    
    #                 X     ,  A         ,  Achild    ,     B      , Achildchild,    Bchild
    myObjects = [Layout(0,0), Layout(1,0), Layout(2,1), Layout(3,0), Layout(4,1), Layout(5,3)]
    indentDic = dict()
    
    extractIndentationLevels(myObjects, indentDic)
                                         
    print indentDic
    
    myObjects = [ Layout(0,0), Layout(5,3), Layout(1,0), Layout(2,1), Layout(3,0), Layout(4,1)]
    indentDic = dict()
    
    extractIndentationLevels(myObjects, indentDic)
    print indentDic
        
    pass
