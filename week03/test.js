var a = 3
console.log(a)

let b = 4 // let은 재선언 불가능
b = 7
console.log(b)

const c = 8 // const는 재선언 및 변수 업데이트 불가


let isMe = true // boolean 자료형
console.log(isMe)


console.log(typeof(c)) // 자료형 확인


// 오브젝트 자료형
const man = {
    name:"안녕",
    age:12,
}

console.log(man.name)


// 정수값을 프롬프트를 통해 입력받음
const pro=parseInt(prompt("나이 입력")) 
console.log(pro) 
// 소수면 소수점 버림이 되고, 문자이면 NaN이 됨 
console.log(typeof(pro))


// 알림창 띄우기
alert("안녕!") 


const mapArray = ["1", "2", "3"] // map 인덱스와 배열 요소 1대1 대응
mapArray.map((x, i) => {
    console.log(x, i)
})



function say(text) { // 함수
    console.log(text)
} 
say("hello!")



const resend = (a, b) => { // resend(a, b) { ... } 와 동일
    return a+b // return 생략 가능
}
const sum = resend(3, 4)
console.log(sum)