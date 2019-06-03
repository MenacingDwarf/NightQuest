import React, {Component} from 'react'
import logo from "../NQlogo.png";

class Header extends Component {
    render() {
        let register_button = this.props.is_auth ? (
            <li onClick={() => this.props.history.push("/personal_area")} className="register-button">
                Личный кабинет
            </li>
        ) : (
            <li onClick={() => this.props.history.push("/register")} className="register-button">
                Зарегистрироваться
            </li>
        );
        return (
            <header className="header">
                <div className="logo">
                    <img src={logo} alt="картинка"/>
                </div>
                <div className="header-right">
                    <ul className="buttons">
                        <li onClick={() => this.props.history.push("/")}>
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
                        {register_button}
                    </ul>
                    <div className="header-text">Night Quest...</div>
                </div>

            </header>
        )
    }
}

export default Header