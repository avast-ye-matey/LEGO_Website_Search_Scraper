


with open('lego_list2.txt', 'w') as f:

    f.write('')
      
    print('What would you like to search?')
    print('What would you like to search?', file=f) 
    print('yo') 
    print('yo', file=f) 
    user_input = input()    
    f.write(user_input)
    f.write('\n')
    print('yo') 
    print('yo', file=f)
    
    
    
    

f.close()