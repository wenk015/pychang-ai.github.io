var i=0;

function count(){
    i=i+1;
    postMessage(i/10);
    setTimeout("count()",100);
}

count();