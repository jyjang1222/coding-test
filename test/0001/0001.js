// 다른 학생 풀이1

// const arr = [
//     [6,5,4,5,5,8],
//     [6,5,6],
//     [6,5,4,5,5],
//     [3,4,5,8,9,3,3,3],
//     [9],
//     [1,4,7]
// ];

// for(let i = 0; i < arr.length; i++){
//     for(let j = i; j < arr.length; j++){
//         if(arr[i].length > arr[j].length){
//             temp = arr[i];
//             arr[i] = arr[j];
//             arr[j] = temp;
//         }
//         for(let k = 1; k <= arr[i].length; k++){
//             if(arr[i][k - 1] === arr[j][k - 1] && arr[i][k] > arr[j][k]){
//                 temp = arr[i];
//                 arr[i] = arr[j];
//                 arr[j] = temp;
//                 if(arr[i].length > arr[j].length){
//                     temp = arr[i];
//                     arr[i] = arr[j];
//                     arr[j] = temp;
//                 }
//                 break;
//             } else if(arr[i][k - 1] > arr[j][k - 1]){
//                 temp = arr[i];
//                 arr[i] = arr[j];
//                 arr[j] = temp;
//                 break;
//             }
//         }
//     }
// }

// console.log(arr);

// 다른 학생 풀이1 수정
const arr = [
    [6,5],
    [6,5,4,5,5,8],
    [6,5,6],
    [0],
    [6,5,4,5,5],
    [3,4,5,8,9,3,3,3],
    [6,5,4],
    [9],
    [1,4,7]
]
// const arr = [
//     [6,5,4,5,5,8],
//     [6,5,6],
//     [6,5,4,5,5],
//     [3,4,5,8,9,3,3,3],
//     [9],
//     [1,4,7]
// ];

for(let i = 0; i < arr.length; i++){
    for(let j = i; j < arr.length; j++){
        for(let k = 1; k <= arr[i].length; k++){
            if(arr[i][k - 1] === arr[j][k - 1] && arr[i][k] > arr[j][k]){
                temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
                if(arr[i].length > arr[j].length){
                    temp = arr[i];
                    arr[i] = arr[j];
                    arr[j] = temp;
                }
                break;
            } else if(arr[i][k - 1] > arr[j][k - 1]){
                temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
                break;
            }
        }
    }
}

console.log(arr);