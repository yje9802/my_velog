<p><a href="https://velog.io/@yje9802/Java-Static-method-Instance-method" color="black">원본 링크</a></p><br><h2 id="static-method">Static method</h2>
<p>Java로 코딩하다 보면 종종 <code>static</code> 키워드가 붙은 메서드를 볼 때가 있다. 이런 메서드를 <code>static</code> 메서드라고 한다. </p>
<p><code>static</code> 메서드의 가장 큰 특징은 <strong>객체 생성 없이도 클래스 이름을 통해 바로 메서드를 참조</strong>할 수 있다는 것이다. </p>
<p>이것이 가능한 이유는 메모리에 있다. <code>static</code> 키워드가 붙게 되면 <strong>JVM이 시작될 때 가장 먼저</strong> 메모리의 Static 영역에 저장되고 프로그램이 종료될 때까지 메모리에 남아있다. (일반적으로 Class는 메모리의 Static 영역에 생성되고, new 연산을 통해 생성한 객체는 Heap 영역에 생성된다.)</p>
<p><img alt="" src="https://velog.velcdn.com/images/yje9802/post/2a94d1e3-21c7-4f18-b208-5ffdadec5cd5/image.png" /></p>
<p>이미지 출처: <a href="https://mangkyu.tistory.com/47">https://mangkyu.tistory.com/47</a></p>
<p>Static 영역은 위 그림처럼 Garbage Collector의 관리 영역 밖에 존재하므로 프로그램의 종료시까지 메모리가 할당된 채로 존재한다. 따라서 Static 영역을 자주 사용하게 되면 시스템의 퍼포먼스에 악영향을 주게 된다는 단점이 있다. </p>
<p>static 메서드는 대체로 인스턴스 변수의 영향을 받지 않으며, 하나의 클래스로부터 생성된 모든 객체에서 동일한 작업을 수행할 수 있도록 하기 위한 목적을 가진다. 그렇기 때문에 <code>Java.lang.Math</code> 클래스처럼 유틸리티 관련 함수들을 static 메서드로 구현하는 편이다. </p>
<p>참고로 <code>this</code>로 참조하기 위한 객체가 존재하지 않기 때문에 <code>this</code> 키워드는 사용할 수 없다.</p>
<h4 id="📌-static-method-예제">📌 static method 예제</h4>
<pre><code class="language-java">class Geek {
    public static String geekName = &quot;&quot;;
    // static method
    public static void geek(String name)
    {
        geekName = name;
    }
}

class GFG {
    public static void main(String[] args)
    {
        // Accessing the static method geek()
        Geek.geek(&quot;vaibhav&quot;);
        System.out.println(Geek.geekName);

        // Accessing the static method geek() by using Object's reference. 
        Geek obj = new Geek();
        obj.geek(&quot;mohit&quot;);
        System.out.println(obj.geekName);
    }
}</code></pre>
<p>예제 출처: <a href="https://www.geeksforgeeks.org/static-method-in-java-with-examples/">https://www.geeksforgeeks.org/static-method-in-java-with-examples/</a></p>
<h3 id="java에서-메인-메서드가-static인-이유">Java에서 메인 메서드가 static인 이유</h3>
<p>메인 메서드는 JVM이 사용하는 프로그램의 시작점이기에 가장 먼저 실행되어야 한다. </p>
<p>만약 static이 아니라면 메인 메서드를 호출할 객체가 존재해야 하지만 JVM이 시작하는 순간에 생성되어 있는 객체는 없을 것이다. </p>
<p>따라서 static 키워드를 사용하여 프로그램이 시작되는 순간 메모리에 올라가 객체 없이도 호출할 수 있게 하는 것이다. </p>
<p>더 자세한 내용은 <a href="https://www.scaler.com/topics/why-main-method-is-static-in-java/">이 사이트</a>를 참고하길 바랍니다. 💪</p>
<hr />
<h2 id="instance-method">Instance method</h2>
<p>static 메서드 이외의 일반적으로 정의하는 메서드를 instance 메서드라고 한다. </p>
<p>static 메서드와의 차이점은 <strong>호출하기 위해서는 반드시 해당 메소드가 정의되어 있는 클래스의 객체를 먼저 생성해주어야 한다</strong>는 점이다. </p>
<p>참고로 인스턴스 메서드라고 해서 매번 객체가 생성될 때마다 함께 생성되는 것은 아니다. 메서드는 메모리에 한 번 할당 되는 것이고, 객체들은 생성되면서 메서드가 메모리 어디에 존재하는지를 알게 된다. 객체는 메서드가 할당된 메모리 주소를 담고 있어 메서드를 호출하면 메모리 주소를 통해 메서드를 호출하는 구조이다. </p>
<h4 id="📌-instance-method-예제">📌 instance method 예제</h4>
<pre><code class="language-java">class GFG { 
    public static void main (String[] args) { 
        // Creating object of the class 
        GFG obj = new GFG();         

        // Calling instance method 
        obj.disp(); 

        System.out.println(&quot;GFG!&quot;); 
    } 

    // Instance method 
    void disp()                                 
    { 
        // Local variable 
        int a = 20;                             
        System.out.println(a); 
    } 
} </code></pre>
<p>예제 출처: <a href="https://www.geeksforgeeks.org/instance-methods-in-java/">https://www.geeksforgeeks.org/instance-methods-in-java/</a></p>
<hr />
<h2 id="static-vs-instance-정리">Static vs Instance 정리</h2>
<h4 id="📌-static">📌 Static</h4>
<ul>
<li><code>ClassName.methodName</code></li>
<li>객체 없이도 클래스 이름만으로 메서드를 호출할 수 있다. </li>
<li>instance 변수 및 메서드는 호출할 수 없다. </li>
</ul>
<h4 id="📌-instance">📌 Instance</h4>
<ul>
<li><code>objectName.methodName</code></li>
<li>호출하기 위해 반드시 객체가 필요하다.</li>
<li>다른 instance 변수 및 메서드, static 변수 및 메서드를 호출할 수 있다.</li>
</ul>
<hr />
<h3 id="📚-reference">📚 Reference</h3>
<h4 id="static-method-1">Static Method</h4>
<ul>
<li><a href="https://mangkyu.tistory.com/47">https://mangkyu.tistory.com/47</a></li>
<li><a href="https://dev-coco.tistory.com/175">https://dev-coco.tistory.com/175</a></li>
</ul>
<h4 id="instance-method-1">Instance Method</h4>
<ul>
<li><a href="https://ykh6242.tistory.com/entry/Java-%EC%9D%B8%EC%8A%A4%ED%84%B4%EC%8A%A4-%EB%A9%94%EC%86%8C%EB%93%9Cinstance-methods%EC%99%80-%EC%A0%95%EC%A0%81-%EB%A9%94%EC%86%8C%EB%93%9Cstatic-methods%EC%9D%98-%EC%B0%A8%EC%9D%B4">https://ykh6242.tistory.com/entry/Java-인스턴스-메소드instance-methods와-정적-메소드static-methods의-차이</a> </li>
</ul>
<h4 id="static-vs-instance">Static vs Instance</h4>
<ul>
<li><a href="https://www.geeksforgeeks.org/static-method-in-java-with-examples/">https://www.geeksforgeeks.org/static-method-in-java-with-examples/</a></li>
</ul>