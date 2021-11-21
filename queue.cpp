#include <iostream>
using namespace std;

#define MaxEl 5

typedef int address;
typedef struct{
    address head, tail;
    string nama[MaxEl], asal[MaxEl];
    int umur[MaxEl];
} Queue;

#define Head(Q) (Q).head
#define Tail(Q) (Q).tail
#define namaHead(Q) (Q).nama[(Q).head]
#define asalHead(Q) (Q).asal[(Q).head]
#define umurHead(Q) (Q).umur[(Q).head]
#define namaTail(Q) (Q).nama[(Q).tail]
#define asalTail(Q) (Q).asal[(Q).tail]
#define umurTail(Q) (Q).umur[(Q).tail]

bool isEmpty(Queue Q){
    return ((Head(Q) == 0) && (Tail(Q) == 0));
}

int nbElmt(Queue Q){
    if(isEmpty(Q)) return 0;

    if(Head(Q) <= Tail(Q)) return (Tail(Q) - Head(Q) + 1);
    else return (MaxEl - Head(Q) + Tail(Q) + 1);
}

bool isFull(Queue Q){
    return (nbElmt(Q) == MaxEl);
}

void createEmpty(Queue *Q){
    Head(*Q) = 0;
    Tail(*Q) = 0;
}

void add(Queue *Q, string nama, string asal, int umur){
    if(isFull(*Q)){
        cout << "Queue Penuh\n";
    } else{
        if(isEmpty(*Q)){
            Head(*Q) = 1;
            Tail(*Q) = 1;
        } else{
            if(Tail(*Q) == MaxEl) Tail(*Q) = 1;
            else Tail(*Q)++;
        } 
    }
        
    namaTail(*Q) = nama;
    asalTail(*Q) = asal;
    umurTail(*Q) = umur;
}

void Del(Queue *Q, int *hapus){
    *hapus = umurHead(*Q);
    if(Tail(*Q) == Head(*Q)){
        Head(*Q) = 0;
        Tail(*Q) = 0;
    } else{
        if(Head(*Q) == MaxEl) Head(*Q) = 1;
        else Head(*Q)++;
    }
        
}


int main(){
    Queue dataAntrian;
    int hapus, n, umur;
    string nama, asal;
    createEmpty(&dataAntrian);
    cin >> n;

    while(n--){
        cout << "Nama : ";
        cin >> nama;

        cout << "Umur(Tahun) : ";
        cin >> umur;
        cin.ignore();
        cout << "Asal : ";
        getline(cin, asal);

        add(&dataAntrian, nama, asal, umur);
        cout << endl;
    }

    int i = 1;
    cout << "No\tNama\tUmur\t\tAsal\n";
    while(Head(dataAntrian)){
        cout << i << "\t" << namaHead(dataAntrian) << "\t" << umurHead(dataAntrian) << "Tahun\t\t" << asalHead(dataAntrian) <<"\n";
        Del(&dataAntrian, &hapus);
    }

    return 0;
}