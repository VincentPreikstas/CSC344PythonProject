#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define C_HURTS_MY_SOUL 100
#define ASCII_CONSTANT 128

void *malloc(size_t size);
void free(void *ptr);
int atoi(const char *str);

//THIS IS THE PATH TO THE SAMPLE INPUT FILE
//"/Users/vincentpreikstas/Desktop/School Classes/CSC 344/C/Actual_Project_For_Submission/test.txt"

struct instruction{
    char writeVal;
    char moveDirection;
    int newState;

};

struct dlln{
    struct dlln* next;
    struct dlln* prev;
    char value;
};


void append(struct dlln *current, char value){
    struct dlln *new = malloc(sizeof(struct dlln));

    while(current->next != NULL){
        current = current->next;
    }
    current->next = new;
    new->value = value;
    new->prev = current;
    new->next = 0;
}


void processTheTape(struct dlln *head, struct instruction **instructionGrid, char *startState, char *endState){

    int currentState = atoi(startState);
    int *localEndState = malloc(sizeof(int));
    char *localVal = malloc(sizeof(char));
    char *localDirection = malloc(sizeof(char));
    int *localNewState = malloc(sizeof(char));

    *localEndState = atoi(endState);

    while(currentState != *localEndState){
        *localVal = instructionGrid[head->value][currentState].writeVal;
        *localDirection = instructionGrid[head->value][currentState].moveDirection;
        *localNewState = instructionGrid[head->value][currentState].newState;

        head->value = *localVal;
        if (strcmp(localDirection, "R") == 0){
            if (head->next == NULL){
                append(head, 'B');
                currentState = *localNewState;
                head = head->next;

            } else{
                head = head->next;
                currentState = *localNewState;
            }
        } else {
            head = head->prev;
            currentState = *localNewState;
        }
    }
    free(localDirection);
    localDirection = NULL;
    free(localVal);
    localVal = NULL;
    free(localNewState);
    localNewState = NULL;
    free(localEndState);
    localEndState = NULL;
}

void displayTape(struct dlln *head){
    printf("Final tape contents: ");
    printf("%c", head->value);
    while(head->next != NULL){

        head = head->next;
        printf("%c", head->value);
    }
    printf("\n");
}


void createThings(FILE *theFile, struct dlln *head, struct instruction **instructionGrid, char *initialTapeConditions, char *numberOfStates, char *startState, char *endState){
    char *instructionHolder = malloc(sizeof(char) * C_HURTS_MY_SOUL);

    strcpy(initialTapeConditions, "");
    strcpy(instructionHolder, "");

    int localStateNum, localStartState, localEndState;
    fgets(initialTapeConditions, C_HURTS_MY_SOUL, theFile);

    fgets(numberOfStates, C_HURTS_MY_SOUL, theFile);
    localStateNum = atoi(numberOfStates);

    fgets(startState, C_HURTS_MY_SOUL, theFile);
    localStartState = atoi(startState);

    fgets(endState, C_HURTS_MY_SOUL, theFile);
    localEndState = atoi(endState);


    int counter = 0;
    char *exitChar = malloc(sizeof(char));
    char *tapeChar = malloc(sizeof(char));

    char *currentState = malloc(sizeof(char));
    char *readVal = malloc(sizeof(char));
    char *writeVal = malloc(sizeof(char));
    char *moveDirection = malloc(sizeof(char));
    char *nextState = malloc(sizeof(char));

    int *currentStateInt = malloc(sizeof(int));
    int *nextStateInt = malloc(sizeof(int));


    strcpy(exitChar, "\r");
    *tapeChar = initialTapeConditions[counter];


    //THIS CREATES THE INITIAL TAPE
    while(strcmp(tapeChar, exitChar) != 0){

        append(head, *tapeChar);
        counter++;
        *tapeChar = initialTapeConditions[counter];
    }

    //THIS READS THE STATE INSTRUCTIONS AND STORES THEM
    while(!feof(theFile)){
        fgets(instructionHolder, C_HURTS_MY_SOUL, theFile);

        *currentState = instructionHolder[1];
        *currentStateInt = atoi(currentState);
        *readVal = instructionHolder[3];
        *writeVal = instructionHolder[8];
        *moveDirection = instructionHolder[10];
        *nextState = instructionHolder[12];
        *nextStateInt = atoi(nextState);

        instructionGrid[*readVal][*currentStateInt].writeVal = *writeVal;
        instructionGrid[*readVal][*currentStateInt].newState = *nextStateInt;
        instructionGrid[*readVal][*currentStateInt].moveDirection = *moveDirection;
    }

    free(instructionHolder);
    instructionHolder = NULL;
    free(exitChar);
    exitChar = NULL;
    free(tapeChar);
    tapeChar = NULL;
    free(readVal);
    readVal = NULL;
    free(writeVal);
    writeVal = NULL;
    free(moveDirection);
    moveDirection = NULL;
    free(nextState);
    nextState = NULL;
    free(currentState);
    currentState = NULL;
    free(currentStateInt);
    currentStateInt = NULL;
    free(nextStateInt);
    nextStateInt = NULL;


}


int main(){

    struct dlln *head = malloc(sizeof(struct dlln));
    struct dlln *writerTracker = malloc(sizeof(struct dlln));
    char *initialTapeConditions = malloc(sizeof(char[C_HURTS_MY_SOUL]));
    char *poorDesignChoices = malloc(sizeof(char[C_HURTS_MY_SOUL]));
    int *poorDesignChoicesInt = malloc(sizeof(int));
    char *numberOfStates = malloc(sizeof(char));
    char *startState = malloc(sizeof(char));
    char *endState = malloc(sizeof(char));
    struct instruction **instructionGrid;

    //GET FILENAME FROM USER
    char *fileName = malloc(sizeof(char[C_HURTS_MY_SOUL]));
    printf("Input file: ");
    scanf("%[^\n]s",fileName);

    printf("Writing tape...\n");

    FILE *filePointer;
    //filePointer = fopen("/Users/vincentpreikstas/Desktop/School Classes/CSC 344/C/Actual_Project_For_Submission/test.txt", "r");
    filePointer = fopen(fileName, "r");

    fgets(initialTapeConditions, C_HURTS_MY_SOUL, filePointer);
    fgets(poorDesignChoices, C_HURTS_MY_SOUL, filePointer);
    *poorDesignChoicesInt = atoi(poorDesignChoices);

    fclose(filePointer);

    instructionGrid = malloc(sizeof(struct instruction *) * ASCII_CONSTANT);
    for (int i = 0; i < ASCII_CONSTANT; i ++){
        instructionGrid[i] = malloc(sizeof(struct instruction) * *poorDesignChoicesInt);
        for (int j = 0; j < *poorDesignChoicesInt; j++){
            instructionGrid[i][j].writeVal = 'B';
            instructionGrid[i][j].moveDirection = 'R';
            instructionGrid[i][j].newState = 0;
        }
    }

    //INITIALIZING HEAD OF TAPE
    head->value = 'A';
    head->prev = 0;
    head->next = 0;

    FILE *filePointer2;
    //filePointer2 = fopen("/Users/vincentpreikstas/Desktop/School Classes/CSC 344/C/Actual_Project_For_Submission/test.txt", "r");
    filePointer2 = fopen(fileName, "r");

    //CALLING MAIN FUNCTIONS
    createThings(filePointer2, head, instructionGrid, initialTapeConditions, numberOfStates, startState, endState);

    processTheTape(head, instructionGrid,startState, endState);

    //DISPLAY THE RESULTS
    printf("Initial tape contents: A%s", initialTapeConditions);
    displayTape(head);

    fclose(filePointer2);
    return 0;
}
