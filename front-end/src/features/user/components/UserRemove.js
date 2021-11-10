import axios from 'axios';
import React, { useState } from 'react';
import { Link, useHistory } from 'react-router-dom';

export default function UserRemove() {
  const [pwd, setPwd] = useState('')
  const sessionUser = JSON.parse(localStorage.getItem('sessionUser'))
  const history = useHistory()
  const SERVER = 'http://localhost:8080'
  
  const handleChange = e => {
    setPwd(e.target.value)
  }
  const handleClick = e => {
    e.preventDefault()
    if(sessionUser.password === pwd){
      axios.delete(`${SERVER}/users/${sessionUser.userId}`)
      .then(res => {
        console.log(res.data)
        localStorage.setItem('sessionUser', '')
        history.push('/')
      })
      .catch(err => console.log(err))
    }else{
      alert('입력된 비밀번호가 틀립니다')
      document.getElementById('password').value = ''
    }
    
  }
  return (
    <div>
      <h1>회원탈퇴</h1>
      <form method="DELETE">
    <ul>
        <li>
              <label>
                    <span>사용자아이디 : {sessionUser.username} </span>
                </label>
            </li>
        <li><label for="pw">비밀번호 확인</label>
        <input type="password" id="password" name="password" onChange={handleChange}/></li>
        <li><input type="submit" value="탈퇴요청" onClick={handleClick}/></li>
        <li><input type="button" value="탈퇴취소" onClick={e => history.push("/users/detail")}/></li>
    </ul>
</form>

    </div>
  );
}