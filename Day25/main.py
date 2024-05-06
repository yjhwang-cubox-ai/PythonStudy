import turtle
import pandas

def main():
    df = pandas.read_csv("Day25/50_states.csv")
    print(df)
    
    screen = turtle.Screen()
    screen.title("U.S. States Game")
    image = "us-states-game-start\\blank_states_img.gif"
    screen.addshape(image)
    turtle.shape(image)
    
    while True:
        answer_state = screen.textinput(title="US states", prompt="input states").title()
        
        if answer_state == "Exit":
            df.to_csv("study.csv")
            break        
        
        user_select = df[df.state == answer_state]
                
        if user_select.empty:
            continue
        
        print(user_select)
        
        x_cor = int(user_select.x.item())
        y_cor = int(user_select.y.item())
        
        point = turtle.Turtle()
        point.hideturtle()
        point.penup()
        point.goto(x_cor,y_cor)
        point.write(user_select.state.item(), align="center")
        
        df.drop(user_select.index,  axis=0, inplace=True)
    

if __name__ == "__main__":
    main()