#सबसे पहले हम एक class  बनाएंगे जो हमे nodes create कर के देगी 
class Node:
    def __init__(self, data): #ये एक constructor method है जो class के objects को initialize करेगी  
        #अब हम node को initialize करेंगे जो data दिया है उसके साथ 
        self.data = data
        #और  ये reference है next node का, जो की फ़िलहाल None है, क्यूंकी यदि linked list मे एक ही item हुआ तो reference None रहेगा  
        self.next = None

#अब दूसरी class बनाएंगे जो की linked list के सारे operations contain करेगी 

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_index(self, data, index):
        if index == 0:
            #पहले एक नई node create करेंगे  
            new_node = Node(data) 
            #अब यदि head node खाली हुई तो मतलब linked list मे एक भी node नहीं है और new_node को head node बना देंगे और function को return कर देंगे 
            if self.head is None:
                self.head = new_node
                return
            #अगर हेड खाली नहीं है, तो हम नया node बनाएंगे और पुराने head को इस नए node के बाद जोड़ देंगे ।  
            else:
                new_node.next = self.head #current head जो है वो नए node का अगला node हो जाएगा   
                self.head = new_node #और फिर नया node नया head बन जाएगा
        
        else:
            #यदि index 0 नहीं है तो, हम एक variable लेंगे जो हमे हमारी current position बताएगा 
            position = 0 
            #सबसे पहले हम linked list के head से शुरूआत करेंगे 
            current_node = self.head
            while (current_node != None and position+1 != index):    #जब तक current_node खाली नहीं है और साथ-ही-साथ हमारी current position 
                                                                     #से एक आगे वाला index दिए गए index के बराबर न हो तो  
                position+=1
                current_node = current_node.next 
            
            #अब यदि linked list मे कोई element बचता है तो  
            if current_node != None:
                #अब हमे सही position मिल गई है, तो एक नई node create करेंगे   
                new_node = Node(data)
                #पुराने node का अगला element नए node का अगला हो जाएगा    
                new_node.next = current_node.next
                #और पुराने node का अगला node नया element हो जाएगा
                current_node.next = new_node

            #यदि linked list मे कोई element नहीं बचता है तो
            else:
                print("Index not present") 

                
    def insert_at_End(self, data):
        #एक नई node create करेंगे 
        new_node = Node(data)
        #यदि linked list के head मे element नहीं है, मतलब linked list खाली है तो    
        if self.head is None:
            #नए element को head मे insert कर देंगे  
            self.head = new_node
            return

        #यदि linked list के head मे element है, तो एक variable लेंगे "current_node" जो हमारी current position store करेगा 
        # initially इसमे head को store करेंगे  
        current_node = self.head
        #अब जब तक हमारी current_node के आगे कोई element हो, जब तक हम बिना कुछ किए आगे बढ़ते जाएंगे   
        while(current_node.next):
            current_node = current_node.next
        #अब हमारे पास current_node के आगे कोई element नहीं है, तो insert कर देंगे     
        current_node.next = new_node


    def delete_at_index(self, index):
        #यदि head मे एक भी element नहीं हो, मतलब linked list खाली है 
        if (self.head == None):
            return
        #अब एक variable "current_node" लिया है, जो हमारी current position store करेगा 
        current_node = self.head
        #starting 0th index से करेंगे 
        position = 0
        #यदि दिया गया index पहला ही element हो तो
        if position == index:      
            if(self.head == None): #और पहला node खाली हो तो, मतलब लिस्ट खाली हो तो 
                return             #सीधे function के बाहर आ जाएंगे 
            self.head = self.head.next
        #यदि index starting index nahi है तो 
        else:
            while(current_node != None and position+1 != index):    #जब तक current_node खाली नहीं है और साथ-ही-साथ हमारी current position 
                                                                    #से एक आगे वाला index दिए गए index के बराबर न हो तो
                position = position+1
                current_node = current_node.next
            #अब यदि linked list मे कोई element बचता है तो
            if current_node != None:
                current_node.next = current_node.next.next #जो element हटाना था वो हट गया और अब उस element के पीछे वाला node उस element के आगे वाले node को point करेगा  
            #अब यदि linked list मे कोई भी element नहीं  बचता है तो
            else:
                print("Index not present")           


    def delete_at_last(self):
        #यदि पहला element ही नहीं हो, मतलब linked list खाली हो 
        if self.head is None:
            return          #function के बाहर आ जाएंगे 
            
        #अब एक variable "current_node" लिया है, जो हमारी current position store करेगा 
        # initially इसमे head को store करेंगे
        current_node = self.head
        #अब जब तक "current_node" के आगे वाली node और साथ-ही-साथ उसके भी आगे वाली node खाली नहीं होती तब तक  
        while (current_node.next != None and current_node.next.next != None):
            #loop को आगे चलाते जाएंगे 
            current_node = current_node.next
        #अब जैसे  ही  "current_node" के आगे वाली node और साथ-ही-साथ उसके भी आगे वाली node खाली मिलती है, मतलब हमे last node मिल गई 
        # अब उसको हम खाली कर देंगे  
        current_node.next = None

        
    def print_Linked_List(self):
        current_node = self.head
        while(current_node):
            print(current_node.data)
            current_node = current_node.next
        
    def lenght(self):
        size = 0
        if(self.head):
            current_node = self.head
            while(current_node):
                size = size+1
                current_node = current_node.next
            return size
        else:
            return 0

llist = LinkedList()
llist.insert_at_index('a',0)
llist.insert_at_index('b',1)
llist.insert_at_index('c',2)
llist.insert_at_index('d',3)
llist.insert_at_index('e',4)
llist.insert_at_End('f')
llist.delete_at_index(2)
llist.print_Linked_List()