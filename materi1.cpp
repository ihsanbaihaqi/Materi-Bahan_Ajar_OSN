#include <iostream>

int main() {  // integer sebagai fungsi yang selalu diakhiri dengan return,
              // main adalah sebuah pintu atau tempat kita memulai program
    std::cout << "Hello, World!" << std::endl; 
    // std adalah standart library berasal dari iostream, 
    // cout atau console out adalah fungsi untuk menampilkan output,
    // << adalah operator untuk mengirim data ke cout, 
    // endl adalah ini adalah akhir dari aliran outputnya
    int a = 10;
    int b = 5;

    std::cout << std::boolalpha;
    std::cout << (a == b) << std::endl;
    std::cout << (a != b) << std::endl;
    std::cout << (a > b) << std::endl;
    return 0;
}