import React, {Component} from 'react'

class Register extends Component {
    render() {
        return (
            <div className="content">
                <div className="row">
                    <div className="col-7">
                        <h5>ЗАРЕГИСТРИРОВАТЬСЯ</h5>
                        <div className="line"/>
                        <div className="row">
                            <div className="col-8">
                                <form action="/register/" method="post">
                                    <label htmlFor="username">Выберите имя пользователя</label>
                                    <input type="text" name={"username"} id={"username"}/>
                                    <label htmlFor="email">Введите электронный адрес</label>
                                    <input type="text" name={"email"} id={"email"}/>
                                    <label htmlFor="password">Выберите пароль</label>
                                    <input type="password" name={"password"} id={"password"}/>
                                    <input type="submit" className={"register-button"} value={"Зарегистрироваться"}/>
                                </form>
                            </div>
                            <div className="col-4 additional-text">
                                Регистрация позволит вам создавать команды и добавляться в уже существующие, принимать
                                участие в квестах и создавать собственные квесты.
                            </div>
                        </div>
                    </div>
                    <div className="col-5">
                        <h5>УЖЕ ЗАРЕГИСТРИРОВАНЫ?</h5>
                        <div className="line"/>
                        <form action="/login/" method="post">
                            <label htmlFor="username">Введите имя пользователя</label>
                            <input type="text" name={"username"} id={"username"}/>
                            <label htmlFor="password">Введите пароль</label>
                            <input type="password" name={"password"} id={"password"}/>
                            <input type="submit" className={"register-button"} value={"Войти"}/>
                        </form>
                    </div>
                </div>
            </div>
        )
    }
}

export default Register