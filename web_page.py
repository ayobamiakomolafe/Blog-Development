
def  main():

    import streamlit as st
    from PIL import Image
    import sys
    from streamlit import cli as stcli
    st.title("TOP 20 RESTAURANTS IN SYDNEY")
    st.write('''Have you ever wanted to grab great food and tried to search for the best local restaurants and food
             spots but you spend way more time reading reviews than actually getting a feed? Well,
             we have created a list of the best local Sydney food spots to save your time.''')

    Quay=st.container()
    La_Salut=st.container()
    Lankan_Filling_Station =st.container()
    Cafe_Paci =st.container()
    Lolas_Level_1 =st.container()
    Saint_Peter =st.container()
    Ursulas_Paddington =st.container()
    Sixpenny =st.container()
    Ester =st.container()
    Sean=st.container()
    LuMi =st.container()
    Odd_Culture_Newtown =st.container()
    Bentley_Restaurant_and_Bar =st.container()
    Hubert =st.container()
    Margaret =st.container()
    Firedoor =st.container()
    Chaco_Bar =st.container()
    Automata =st.container()
    William_Street=st.container()
    Sang_by_Mabasa =st.container()



    names=["1.\xa0Quay",  "2.\xa0La Salut", "3. Lankan Filling Station" ,"4.\xa0Café Paci", "5.\xa0Lola's Level 1", "6.\xa0Saint Peter","7.\xa0Ursula's Paddington", "8.\xa0Sixpenny","9.\xa0Ester",
           "10.\xa0Sean's","11.\xa0LuMi","12.\xa0Odd Culture Newtown", "13.\xa0Bentley Restaurant and Bar","14.\xa0Hubert", "15.\xa0Margaret","16.\xa0Firedoor",
           "17.\xa0Chaco Bar","18.\xa0Automata", "19.\xa010 William Street","20.\xa0Sáng by Mabasa"]


    
    website=['If you fancy a fine dining experience with panoramic views of Sydney harbour and Sydney’s pristine waters, this is a great option for you. They offer an extensive menu by Australian chef Peter Gilmore.\n', 'This spot is inspired by Barcelona, Spain. It offers a menu by chef Scott McComas-Williams bringing a taste of Spain to Redfern, Sydney. It showcases the peak of Australian produce.\xa0\n', 'This is a casual eatery, where our food is inspired by traditional Sri Lankan flavours seen through the eyes of Australia. It features a Modern restaurant serving Sri Lankan pancakes, curries & drinks in an easygoing ambience by chef and owner O Tama Carey.\n', 'This hip industrial-chic restaurant offers a gourmet menu of Modern Australian dishes with a twist by finnish-bornn chef Pasi Petanen. The menu explores his Finnish roots with influence drawing from Mexican and Vietnamese cuisine.\n', 'The South European-inspired menu features generously portioned dishes with a clever mix of sharing. The adage to food is to be free spirited, so think of the flavours of Italy, Spain, Greece and the Mediterranean Coast.\n', 'A highly rated seafood restaurant with a fresh and unique menu by Chef Josh Niland. Dry-aged fish is worth a try and is what Niland is renowned for, this restaurant gives quite the experience with the Chef cooking in front of you.\n', 'At his first solo restaurant, acclaimed chef Phil Wood explores and expands Australian cuisine with a produce-driven menu combining classic European cooking. Private dining and group bookings are also available.\n', 'Chefs Daniel Puskas and Anthony Schifilliti lead the kitchen in utilising homegrown local suppliers, growers and producers to focus on creating a narrative around all things that make-up Australia. The restaurant is a cosy space which serves modern Australian food. Reservations are required and events can be held here.\n', 'Trendy restaurant executing eclectic dishes in a concrete-walled space with a wood-fired oven. Australian cuisine\n', 'Small, market-driven restaurant with tasting menus and set meals, plus outdoor seats and surf views. Affectionately known as ‘Sean’s’ since opening in 1993, our little ‘salty jewel’ of a restaurant serves comforting home–style food balanced with modern tastes. A small but affordable spot.']
    address=[' Upper Level Overseas Passenger Terminal, The Rocks\n', ' 305 Cleveland St, Redfern\xa0\n', ' Ground Floor, 58 Riley St, Darlinghurst\xa0\n', ' 131 King street, Newtown\n', ' Level 1/180/186 Campbell Parade, Bondi Beach\n', ' 362 Oxford St, Paddington\n', ' 92 Hargrave St, Paddington\xa0\n', ' 83 Percival Rd, Stanmore\n', ' 46_52 meagher st, chippendale\xa0\n', ' 270 Campbell Parade, North Bondi\xa0\n']
    rating=['4.5 stars\n', '4.7 stars\n', '4.2 stars\n', '4.7 stars\n', '3.6 stars\n', '4.6 stars\n', '4.5 stars\n', '4.8 stars\n', '4.5 stars\n', '4.1 stars\n']


    

    
    with Quay:
        st.header(names[0])
        st.markdown("##### Address :   "+ address[0])
        st.markdown("##### Star-Rating :  "+ rating[0])
        col1,col2,col3,col4, col5=st.columns(5)
        img=Image.open(names[0]+ str(1) + '.JPG')
        col1.image(img, use_column_width=True)
        img=Image.open(names[0]+ str(2)+ '.JPG')
        col2.image(img, use_column_width=True)
        img=Image.open(names[0]+ str(3)+ '.JPG')
        col3.image(img, use_column_width=True)
        img=Image.open(names[0]+ str(4)+ '.JPG')
        col4.image(img, use_column_width=True)
        img=Image.open(names[0]+ str(5)+ '.JPG')
        col5.image(img, use_column_width=True)
        if st.button("Read More About "+ names[0][3:]):
            st.write(website[0])
            
            
            

    with La_Salut:
        st.header(names[1])
        st.markdown("##### Address :   "+ address[1])
        st.markdown("##### Star-Rating :  "+ rating[1])
        col1,col2,col3=st.columns(3)
        img=Image.open(names[1]+ str(1) + '.JPG')
        col1.image(img, use_column_width=True)
        img=Image.open(names[1]+ str(2)+ '.JPG')
        col2.image(img, use_column_width=True)
        img=Image.open(names[1]+ str(3)+ '.JPG')
        col3.image(img,use_column_width=True)
        if st.button("Read More About "+ names[1][3:]):
            st.write(website[1])

    with Lankan_Filling_Station:
        st.header(names[2])
        st.markdown("##### Address :   "+ address[2])
        st.markdown("##### Star-Rating :  "+ rating[2])
        col1,col2,col3, col4, col5=st.columns(5)
        img=Image.open(names[2] +  str(2)+ '.JPG')
        col1.image(img, use_column_width=True)
        img=Image.open(names[2]+ str(2)+ '.JPG')
        col2.image(img, use_column_width=True)
        img=Image.open(names[2]+ str(3)+ '.JPG')
        col3.image(img, use_column_width=True)
        img=Image.open(names[2]+ str(4)+ '.JPG')
        col4.image(img, use_column_width=True)
        img=Image.open(names[2]+ str(5)+ '.JPG')
        col5.image(img, use_column_width=True)
        if st.button("Read More About "+ names[2][3:]):
            st.write(website[2])

    with Cafe_Paci:
        st.header(names[3])
        st.markdown("##### Address :   "+ address[3])
        st.markdown("##### Star-Rating :  "+ rating[3])
        col1,col2,col3, col4, col5=st.columns(5)
        img=Image.open(names[3]+ str(1)+ '.JPG')
        col1.image(img, use_column_width=True)
        img=Image.open(names[3]+ str(2)+ '.JPG')
        col2.image(img, use_column_width=True)
        img=Image.open(names[3]+ str(3)+ '.JPG')
        col3.image(img, use_column_width=True)
        img=Image.open(names[3]+ str(4)+ '.JPG')
        col4.image(img, use_column_width=True)
        img=Image.open(names[3]+ str(5)+ '.JPG')
        col5.image(img, use_column_width=True)
        if st.button("Read More About "+ names[3][3:]):
            st.write(website[3])

    with Lolas_Level_1:
        name= names[4]
        st.header(names[4])
        st.markdown("##### Address :   "+ address[4])
        st.markdown("##### Star-Rating :  "+ rating[4])
        col1,col2,col3, col4, col5=st.columns(5)
        img=Image.open(name+ str(1)+ '.JPG')
        col1.image(img, use_column_width=True)
        img=Image.open(name+ str(2)+ '.JPG')
        col2.image(img, use_column_width=True)
        img=Image.open(name+ str(3)+ '.JPG')
        col3.image(img, use_column_width=True)
        img=Image.open(name+ str(4)+ '.JPG')
        col4.image(img, use_column_width=True)
        img=Image.open(name+ str(5)+ '.JPG')
        col5.image(img, use_column_width=True)
        if st.button("Read More About "+ names[4][3:]):
            st.write(website[4])

        
    with Saint_Peter:
        name= names[5]
        st.header(names[5])
        st.markdown("##### Address :   "+ address[5])
        st.markdown("##### Star-Rating :  "+ rating[5])
        col1,col2,col3, col4, col5=st.columns(5)
        img=Image.open(name+ str(1)+ '.JPG')
        col1.image(img, use_column_width=True)
        img=Image.open(name+ str(2)+ '.JPG')
        col2.image(img, use_column_width=True)
        img=Image.open(name+ str(3)+ '.JPG')
        col3.image(img, use_column_width=True)
        img=Image.open(name+ str(4)+ '.JPG')
        col4.image(img, use_column_width=True)
        img=Image.open(name+ str(5)+ '.JPG')
        col5.image(img, use_column_width=True)
        if st.button("Read More About "+ names[5][3:]):
            st.write(website[5])

    with Ursulas_Paddington:
        name= names[6]
        st.header(names[6])
        st.markdown("##### Address :   "+ address[6])
        st.markdown("##### Star-Rating :  "+ rating[6])
        col1,col2,col3, col4, col5=st.columns(5)
        img=Image.open(name+ str(1)+ '.JPG')
        col1.image(img, use_column_width=True)
        img=Image.open(name+ str(2)+ '.JPG')
        col2.image(img, use_column_width=True)
        img=Image.open(name+ str(3)+ '.JPG')
        col3.image(img, use_column_width=True)
        img=Image.open(name+ str(4)+ '.JPG')
        col4.image(img, use_column_width=True)
        if st.button("Read More About "+ names[6][3:]):
            st.write(website[6])
        

    with Sixpenny:
        name= names[7]
        st.header(names[7])
        st.markdown("##### Address :   "+ address[7])
        st.markdown("##### Star-Rating :  "+ rating[7])
        col1,col2,col3, col4, col5=st.columns(5)
        img=Image.open(name+ str(1)+ '.JPG')
        col1.image(img, use_column_width=True)
        img=Image.open(name+ str(2)+ '.JPG')
        col2.image(img, use_column_width=True)
        img=Image.open(name+ str(3)+ '.JPG')
        col3.image(img, use_column_width=True)
        img=Image.open(name+ str(4)+ '.JPG')
        col4.image(img, use_column_width=True)
        img=Image.open(name+ str(5)+ '.JPG')
        col5.image(img, use_column_width=True)
        if st.button("Read More About "+ names[7][3:]):
            st.write(website[7])

    with Ester:
        name= names[8]
        st.header(names[8])
        st.markdown("##### Address :   "+ address[8])
        st.markdown("##### Star-Rating :  "+ rating[8])
        col1,col2,col3, col4, col5=st.columns(5)
        img=Image.open(name+ str(1)+ '.JPG')
        col1.image(img, use_column_width=True)
        img=Image.open(name+ str(2)+ '.JPG')
        col2.image(img, use_column_width=True)
        img=Image.open(name+ str(3)+ '.JPG')
        col3.image(img, use_column_width=True)
        img=Image.open(name+ str(4)+ '.JPG')
        col4.image(img, use_column_width=True)
        img=Image.open(name+ str(5)+ '.JPG')
        col5.image(img, use_column_width=True)
        if st.button("Read More About "+ names[8][3:]):
            st.write(website[8])

    with Sean:
        name= names[9]
        st.header(names[9])
        st.markdown("##### Address :   "+ address[9])
        st.markdown("##### Star-Rating :  "+ rating[9])
        col1,col2,col3, col4, col5=st.columns(5)
        img=Image.open(name+ str(1)+ '.JPG')
        col1.image(img, use_column_width=True)
        img=Image.open(name+ str(2)+ '.JPG')
        col2.image(img, use_column_width=True)
        img=Image.open(name+ str(3)+ '.JPG')
        col3.image(img, use_column_width=True)
        img=Image.open(name+ str(4)+ '.JPG')
        col4.image(img, use_column_width=True)
        img=Image.open(name+ str(5)+ '.JPG')
        col5.image(img, use_column_width=True)
        if st.button("Read More About "+ names[9][3:]):
            st.write(website[9])
        

    with LuMi:
        name= names[10]
        st.header(names[10])
        
        col1,col2,col3, col4, col5=st.columns(5)
        img=Image.open(name+ str(1)+ '.JPG')
        col1.image(img, use_column_width=True)
        img=Image.open(name+ str(2)+ '.JPG')
        col2.image(img, use_column_width=True)
        img=Image.open(name+ str(3)+ '.JPG')
        col3.image(img, use_column_width=True)
        img=Image.open(name+ str(4)+ '.JPG')
        col4.image(img, use_column_width=True)
        img=Image.open(name+ str(5)+ '.JPG')
        col5.image(img, use_column_width=True)
        
    with Odd_Culture_Newtown:
        name= names[11]
        st.header(names[11])
        
        col1,col2,col3, col4, col5=st.columns(5)
        img=Image.open(name+ str(1)+ '.JPG')
        col1.image(img, use_column_width=True)
        img=Image.open(name+ str(2)+ '.JPG')
        col2.image(img, use_column_width=True)
        img=Image.open(name+ str(3)+ '.JPG')
        col3.image(img, use_column_width=True)
        img=Image.open(name+ str(4)+ '.JPG')
        col4.image(img, use_column_width=True)
        img=Image.open(name+ str(5)+ '.JPG')
        col5.image(img, use_column_width=True)
        
    with Bentley_Restaurant_and_Bar:
        name= names[12]
        st.header(names[12])
        
        col1,col2,col3, col4, col5=st.columns(5)
        img=Image.open(name+ str(1)+ '.JPG')
        col1.image(img, use_column_width=True)
        img=Image.open(name+ str(2)+ '.JPG')
        col2.image(img, use_column_width=True)
        img=Image.open(name+ str(3)+ '.JPG')
        col3.image(img, use_column_width=True)
        img=Image.open(name+ str(4)+ '.JPG')
        col4.image(img, use_column_width=True)
        img=Image.open(name+ str(5)+ '.JPG')
        col5.image(img, use_column_width=True)
        
    with Hubert:
        name= names[13]
        st.header(names[13])
        
        col1,col2,col3, col4, col5=st.columns(5)
        img=Image.open(name+ str(1)+ '.JPG')
        col1.image(img, use_column_width=True)
        img=Image.open(name+ str(2)+ '.JPG')
        col2.image(img, use_column_width=True)
        img=Image.open(name+ str(3)+ '.JPG')
        col3.image(img, use_column_width=True)
        img=Image.open(name+ str(4)+ '.JPG')
        col4.image(img, use_column_width=True)
        img=Image.open(name+ str(5)+ '.JPG')
        col5.image(img, use_column_width=True)

    with Margaret:
        name= names[14]
        st.header(names[14])
        
        col1,col2,col3, col4, col5=st.columns(5)
        img=Image.open(name+ str(1)+ '.JPG')
        col1.image(img, use_column_width=True)
        img=Image.open(name+ str(2)+ '.JPG')
        col2.image(img, use_column_width=True)
        img=Image.open(name+ str(3)+ '.JPG')
        col3.image(img, use_column_width=True)
        img=Image.open(name+ str(4)+ '.JPG')
        col4.image(img, use_column_width=True)
        img=Image.open(name+ str(5)+ '.JPG')
        col5.image(img, use_column_width=True)
        
    with Firedoor:
        name= names[15]
        st.header(names[15])
        
        col1,col2,col3, col4, col5=st.columns(5)
        img=Image.open(name+ str(1)+ '.JPG')
        col1.image(img, use_column_width=True)
        img=Image.open(name+ str(2)+ '.JPG')
        col2.image(img, use_column_width=True)
        img=Image.open(name+ str(3)+ '.JPG')
        col3.image(img, use_column_width=True)
        img=Image.open(name+ str(4)+ '.JPG')
        col4.image(img, use_column_width=True)
        img=Image.open(name+ str(5)+ '.JPG')
        col5.image(img, use_column_width=True)
        
    with Chaco_Bar:
        name= names[16]
        st.header(names[16])
        
        col1,col2,col3, col4, col5=st.columns(5)
        img=Image.open(name+ str(1)+ '.JPG')
        col1.image(img, use_column_width=True)
        img=Image.open(name+ str(2)+ '.JPG')
        col2.image(img, use_column_width=True)
        img=Image.open(name+ str(3)+ '.JPG')
        col3.image(img, use_column_width=True)
        img=Image.open(name+ str(4)+ '.JPG')
        col4.image(img, use_column_width=True)
        img=Image.open(name+ str(5)+ '.JPG')
        col5.image(img, use_column_width=True)
        
    with Automata:
        name= names[17]
        st.header(names[17])
        
        col1,col2,col3, col4, col5=st.columns(5)
        img=Image.open(name+ str(1)+ '.JPG')
        col1.image(img, use_column_width=True)
        img=Image.open(name+ str(2)+ '.JPG')
        col2.image(img, use_column_width=True)
        img=Image.open(name+ str(3)+ '.JPG')
        col3.image(img, use_column_width=True)
        img=Image.open(name+ str(4)+ '.JPG')
        col4.image(img, use_column_width=True)
        img=Image.open(name+ str(5)+ '.JPG')
        col5.image(img, use_column_width=True)
        
    with William_Street:
        name= names[18]
        st.header(names[18])
        
        col1,col2,col3, col4, col5=st.columns(5)
        img=Image.open(name+ str(1)+ '.JPG')
        col1.image(img, use_column_width=True)
        img=Image.open(name+ str(2)+ '.JPG')
        col2.image(img, use_column_width=True)
        img=Image.open(name+ str(3)+ '.JPG')
        col3.image(img, use_column_width=True)
        img=Image.open(name+ str(4)+ '.JPG')
        col4.image(img, use_column_width=True)
        img=Image.open(name+ str(5)+ '.JPG')
        col5.image(img, use_column_width=True)
        
    with Sang_by_Mabasa:
        name= names[19]
        st.header(names[19])
        
        col1,col2,col3, col4, col5=st.columns(5)
        img=Image.open(name+ str(1)+ '.JPG')
        col1.image(img, use_column_width=True)
        img=Image.open(name+ str(2)+ '.JPG')
        col2.image(img, use_column_width=True)
        img=Image.open(name+ str(3)+ '.JPG')
        col3.image(img, use_column_width=True)
        img=Image.open(name+ str(4)+ '.JPG')
        col4.image(img, use_column_width=True)
        img=Image.open(name+ str(5)+ '.JPG')
        col5.image(img, use_column_width=True)

import streamlit 
import sys
from streamlit import cli as stcli
if __name__ == '__main__':
    if streamlit._is_running_with_streamlit:
        main()
    else:
        sys.argv = ["streamlit", "run", sys.argv[0]]
        sys.exit(stcli.main())


















    
    
    
    
    

