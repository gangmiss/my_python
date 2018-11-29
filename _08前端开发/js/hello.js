
/*JavaScript五种基本数据类型：number,string,boolean,undefined,null，一种复合类型：object
    命名规范：
        1.区分大小写
        2.必须以字母或下划线或$开头
        3.其他字符可以是字母，数字，下划线，美元符
* */

//文档对象document


window.onload=function () {
    alert('2222222222222')
    //生成标签元素对象
    var oDiv=document.getElementById('div1');
    //对象属性一般用.引用，也可以用['']或者[]引用

    //读取属性
    oDiv.style.fontSize='12px';
    oDiv.style.backgroundColor='#ff0000';
    oDiv.className='更改成其他的css样式.css';

    //    写入属性值
    oDiv.innerHTML="写入一段话";
    oDiv.innerHTML="<a href='http://www.baidu.com'>百度网</a>";

}

function click11() {
        alert('kkkkkkkkkkkkk')
    }
