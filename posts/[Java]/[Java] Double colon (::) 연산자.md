<p><a href="https://velog.io/@yje9802/Java-Double-colon-%EC%97%B0%EC%82%B0%EC%9E%90" color="black">원본 링크</a></p><br><h1 id="double-colon-operator-in-java">Double colon(::) operator in Java</h1>
<blockquote>
<p><strong>Method reference operator</strong>
메서드 참조 연산자</p>
</blockquote>
<p>자바에서 람다식을 쓰다보면 보게 되는 이 <code>::</code> 는 무엇일까? </p>
<p>자바8에서 도입된 연산자로 메서드 참조 연산자라고도 부른다. 람다식과 동일한 역할을 하지만, 람다식과 다르게 매개변수를 작성하지 않는다는 차이점이 있다. </p>
<p>기본적인 람다식을 더블 콜론을 사용하여 바꾸면 이렇게 된다.</p>
<pre><code class="language-java">// lambda
(a, b) -&gt; ClassName.methodName(a, b)
// double colon
className::methodName</code></pre>
<h3 id="✅-더블-콜론을-쓸-수-있는-경우">✅ 더블 콜론(::)을 쓸 수 있는 경우</h3>
<h4 id="▪︎-static-메서드-참조">▪︎ static 메서드 참조</h4>
<p><code>::</code>을 이용해 static 메서드를 호출할 수 있다. 
<code>ClassName::staticMethod</code> </p>
<pre><code class="language-java">...
public static void main(String[] args) 
    { 
        List&lt;String&gt; list = new ArrayList&lt;String&gt;(); 
        list.add(&quot;Taylor&quot;); 
        list.add(&quot;Swift&quot;);

        // lambda로 호출
        list.forEach(s -&gt; Call.someFuntion(s));
        // 더블 콜론으로 호출
        list.forEach(Call::someFunction);
    } 
...
class Call { 
    // static function to be called 
    static void someFunction(String s) { 
        System.out.println(s); 
    } 
} </code></pre>
<h4 id="▪︎-인스턴스-메서드-참조">▪︎ 인스턴스 메서드 참조</h4>
<p><code>objectName::instanceMethod</code> 구문을 통해 인스턴스 메서드를 호출할 수 있다. </p>
<pre><code class="language-java">...
public static void main(String[] args) 
    { 
        List&lt;String&gt; list = new ArrayList&lt;String&gt;(); 
        list.add(&quot;Taylor&quot;); 
        list.add(&quot;Swift&quot;);

        Call call = new Call();
        // lambda로 호출
        list.forEach(s -&gt; call.someFuntion(s));
        // 더블 콜론으로 호출
        list.forEach(call::someFunction);
        // 이렇게도 가능하다
        list.forEach((new Call())::someFunction);
    } 
...
class Call { 
    // instance method to be called 
    void someFunction(String s) { 
        System.out.println(s); 
    } 
} </code></pre>
<h4 id="▪︎-임의의-특정-객체의-인스턴스-메서드-참조">▪︎ 임의의 특정 객체의 인스턴스 메서드 참조</h4>
<pre><code class="language-java">class Test {  
    String str=null; 
    Test(String s) { 
        this.str=s; 
    } 
    // instance function to be called  
    void someFunction() {  
        System.out.println(this.str);  
    }  
}
class Taylor {  
    public static void main(String[] args)  
    {  
        List&lt;Test&gt; list = new ArrayList&lt;Test&gt;();  
        list.add(new Test(&quot;Taylor&quot;));  
        list.add(new Test(&quot;Swift&quot;));   

        list.forEach(Test::someFunction);  
    }  
} </code></pre>
<h4 id="▪︎-객체-생성자-참조">▪︎ 객체 생성자 참조</h4>
<p>원래는 <code>(a, b) -&gt; {return new ClassName(a, b)}</code> 이렇게 되야할 구문도 더블 콜론을 사용하여 <code>ClassName::new</code> 이런 식으로 사용할 수 있다.</p>
<pre><code class="language-java">class Taylor { 
    // Class constructor 
    public Call(String s) { 
        System.out.println(&quot;Hello &quot; + s); 
    } 

    public static void main(String[] args) { 
        List&lt;String&gt; list = new ArrayList&lt;String&gt;(); 
        list.add(&quot;Taylor&quot;); 
        list.add(&quot;Swift&quot;); 

        // call the class constructor 
        list.forEach(Call::new); 
    } 
} </code></pre>
<h4 id="▪︎-super-메서드-참조">▪︎ super 메서드 참조</h4>
<p>더블 콜론을 사용해 super 메서드도 호출할 수 있다. </p>
<pre><code class="language-java">class Test { 
    // super function to be called 
    String print(String str) { 
        return (&quot;Hello &quot; + str + &quot;\n&quot;); 
    } 
} 
class Taylor extends Test { 
    // instance method to override super method 
    @Override
    String print(String s) 
    { 
        // call the super method using double colon operator 
        Function&lt;String, String&gt; 
            func = super::print; 

        String newValue = func.apply(s); 
        newValue += &quot;Bye &quot; + s + &quot;\n&quot;; 
        System.out.println(newValue); 

        return newValue; 
    } 
}</code></pre>
<hr />
<h3 id="📚-reference">📚 Reference</h3>
<ul>
<li><a href="https://www.geeksforgeeks.org/double-colon-operator-in-java/">GeeksforGeeks - Double colon (::) operator in Java</a></li>
<li><a href="https://lasbe.tistory.com/75">[Java/자바] 메소드 참조(method reference), &quot;::&quot; 사용법</a></li>
<li><a href="https://developer-talk.tistory.com/462">[Java]메서드 참조(Method reference)</a></li>
</ul>