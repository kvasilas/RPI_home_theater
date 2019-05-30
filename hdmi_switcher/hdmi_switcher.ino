// Constant Parameters
const int INPUTCOUNT = 3;
const int button_pin = ;
const int media_pin = ;
const int xbox_pin = ;
const int wii_pin = ;

// Variable positions
int current;
int target;

void setup{
    //initialize Pin modes
    pinMode(button_pin, OUTPUT);
    pinMode(media_pin, INPUT);
    pinMode(xbox_pin, INPUT);
    pinMode(wii_pin, INPUT);

    //Open Serial Communication
    Serial.begin(9600);
    delay(500);
    Serial.println("**  Serial Comm Set Up!  **");

    //Setup Moduless
    check_state();
}

void loop{
    if(Serial.available()){
        int input = Serial.read();
        switch(input){
            case 'c':
                current_state();
                break;
            case 'b':
                button_press();
                break;
            case '1':
                target = media_pin;
                switch_input();
                break;
            case '2':
                target = xbox_pin;
                switch_input();
                break;
            case '3':
                target = wii_pin;
                switch_input();
                break;
        }
    }
}

void check_state(){
    //read input pins to determine current state
    // maybe assign digitalRead(pin) to a variable p_state?
    if(digitalRead(wii_pin) == HIGH){
        current = wii_pin;
    }
    else if(digitalRead(xbox_pin) == HIGH){
        current = xbox_pin;
    }
    else{
        current = media_pin;
    }
}

void button_press(){
    digitalWrite(button_pin, HIGH);
    delay(500);
    digitalWrite(button_pin, LOW);
}

void switch_input(){
    check_state();
    while(target != current){
        button_press();
        check_state();
    }
    check_state();
}
