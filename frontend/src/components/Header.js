import React, {Component} from 'react'
import logo from "../NQlogo.png";

class Header extends Component {
    render() {
        return (
            <header className="header">
                <div className="logo">
                    <img src={logo} alt="картинка"/>
                </div>
                <div className="header-right">
                    <ul className="buttons">
                        <li onClick={() => window.location = "/"}>
                            <div className="menu-button">Главная</div>
                            <div className="underline"/>
                        </li>
                        <li onClick={() => window.location = "/teams"}>
                            <div className="menu-button">Команды</div>
                            <div className="underline"/>
                        </li>
                        <li onClick={() => window.location = "/quests"}>
                            <div className="menu-button">Квесты</div>
                            <div className="underline"/>
                        </li>
                        <li onClick={() => window.location = "/register"} className="register-button">
                            Зарегистрироваться
                        </li>
                    </ul>
                    <div className="header-text">Night Quest...</div>
                </div>

            </header>
        )
    }
}

export default Header