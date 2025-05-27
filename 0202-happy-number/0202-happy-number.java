class Solution {
    public boolean isHappy(int temp) {
     HashSet<Integer> hs=new HashSet<>();
     while(true){
        int s=0;
        while(temp!=0){
            int a=temp%10;
            s+=a*a;
            temp/=10;
        }
        temp=s;
        if(s==1){
            return true;
        }
        if(hs.contains(temp)){
            return false;
        }
        hs.add(temp);
     }   
    }
}