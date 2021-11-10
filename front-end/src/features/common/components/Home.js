import React from 'react';
import { useHistory  } from 'react-router-dom';
export default function Home() {
  const history = useHistory()
  const sessionUser = localStorage.getItem("sessionUser")
  const logout = e => {
    e.preventDefault()
    localStorage.setItem('sessionUser','')
    history.push('/')
}
  return (
    <div>
      {sessionUser !== '' && <input type="button" value="로그아웃" onClick={logout}/>}
      <h1>시간이란...</h1>
      <p>내일 죽을 것처럼 오늘을 살고 
          영원히 살 것처럼 내일을 꿈꾸어라.</p>
       {sessionUser !== '' ?<h1>{sessionUser.username} 접속중 ...</h1>
       :
       <><button onClick = {e => history.push('/users/add')}>회원가입</button>
       <button onClick = {e => history.push('/users/login')}>로그인</button></>}
    </div>
  );
}