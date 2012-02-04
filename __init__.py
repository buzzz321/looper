# -*- coding: utf-8 -*-
class Layout:
    def __init__(self, myid, parentId, children = None):
        self.myid = myid
        self.parentId = parentId
        self.children = children or []
        
    def hasParent(self):
        return self.myid != self.parentId
    
    def hasChildren(self):
        return len(self.children) > 0
    
    def __str__(self):
        return "Layout<myid=" + `self.myid` + " parentid=" + `self.parentId` +" "+  `self.children` + ">"
    
    def __repr__(self):
        return "Layout<myid=" + `self.myid` + " parentid=" + `self.parentId`  +" "+ `self.children` + ">"

class Indenter:
    def __init__(self, layout, indentLevel):
        self.layout = layout
        self.indentLevel = indentLevel
        
    def __str__(self):
        return "Indenter." + `self.layout` + " indentlevel =" + `self.indentLevel`
    
    def __repr__(self):
        return "Indenter." + `self.layout` + " indentlevel =" + `self.indentLevel`

def indent(objects, indentLevel, flattened):
    if objects == []:
        return None
    
    indenter = objects[0]
    indenter.indentLevel = indentLevel
    
    print `indenter.layout.myid` + " has level: " + `indentLevel`
    
    flattened.append({indenter.layout.myid : indentLevel})
    
    indent(objects[1:], indenter.indentLevel , flattened)
    indent(indenter.layout.children, indenter.indentLevel + 1, flattened)
    

#                   X                ,          A             ,          Achild                  B              ,          Achilchild    ,          Bchild
#objectList = [Indenter(Layout(0,0),0), Indenter(Layout(1,0),0), Indenter(Layout(2,1),0), Indenter(Layout(3,0),0), Indenter(Layout(4,1),0), Indenter(Layout(5,3),0)]
#                          X                    A                          B
objectList = [Indenter(Layout(0,0,[Indenter(Layout(1,0),0),Indenter(Layout(3,0),0)]),0)]
#                                                      Achild       ,            Achildchild
objectList[0].layout.children[0].layout.children.append(Indenter(Layout(2,1,[Indenter(Layout(4,1),0)]),0))
#                                                        Bchild
objectList[0].layout.children[1].layout.children.append(Indenter(Layout(5,3),0))

flattened = []
print indent(objectList, 0, flattened)

print flattened
print objectList
