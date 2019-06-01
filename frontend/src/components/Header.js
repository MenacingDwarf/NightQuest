import React, {Component} from 'react'
import logo from "../NQlogo.png";

class Header extends Component {
    render() {
        return (
            <div className="header">
                <div className="logo">
                    <img src={logo} alt="картинка"/>
                </div>
                <div className="header-right">
                    <ul className="buttons">
                        <li>
                            <div className="button">Главная</div>
                            <div className="underline"/>
                        </li>
                        <li>
                            <div className="button">Команды</div>
                            <div className="underline"/>
                        </li>
                        <li>
                            <div className="button">Квесты</div>
                            <div className="underline"/>
                        </li>
                        <li className="register">
                            Зарегистрироваться
                        </li>
                    </ul>
                    <div className="header-text">Night Quest...</div>
                </div>

            </div>
        )
    }
}

export default Header