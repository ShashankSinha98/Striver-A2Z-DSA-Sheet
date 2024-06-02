class StackUsingArrays {
    public static void main(String[] args) {
        Solution.Stack st = new Solution.Stack(10);
        st.push(1);
        st.push(2);
        st.pop();
        st.pop();
        System.out.println(st.isEmpty());

    }

    class Solution{
        static class Stack {
            private int[] stackArray;
            private int top;

            Stack(int capacity) {
                stackArray = new int[capacity+1];
                top = -1;
            }
            public void push(int num) {
                if(top == this.stackArray.length-1) {
                    return;
                }

                this.stackArray[++this.top] = num;
            }

            public int pop() {
                if(top==-1) {
                    return -1;
                }
                int item = this.stackArray[this.top--];
                return item;
            }
            public int top() {
                return (top >= 0) ? this.stackArray[top] : -1;
            }
            public int isEmpty() {
                return (top == -1) ? 1 : 0;
            }
            public int isFull() {
                return (top == this.stackArray.length-1) ? 1:0;
            }
        }
    }
}