package java;

import java.util.Arrays;

//동일성 비교, 동등성 비교의 다른점을 이해해야한다.

//동일성 비교는  == 객체 인스턴스의 주소 값을 비교한다.
//동등성 비교는 equals() 메소드를 사용해서 객체 내부의 값을 비교한다.
class Solution {
    public String solution(String[] participant, String[] completion) {
        //정렬을 하여 탐색속도를 줄임.
        //데이터가 무수히 늘어날 경우, 과부하 방지
        Arrays.sort(participant);
        Arrays.sort(completion);
        int i = 0;

        for(i=0; i<participant.length; i++){
            if(!participant[i].equals(completion[i])){
                return participant[i];
            }
        }
        return participant[i];
    }
}