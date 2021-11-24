The BOF challenge is prone to Array Out of Bounds in C/C++ 
The BOF challenge if passed with array larger than the size its capable to handle leads to Undefined Behaviour. And also with infinite loop when passed with
alphabets.


arr[10] = 11;  //can lead to segmentation fault in C 

The answer.sh bash script passes the two parameters requested by the application and then causes the crash by providing a value not adjustable in arr[] hence leading to a Undefined Behaviour/Segmentation Fault.
