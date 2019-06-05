import React, {Component} from 'react'

class HeaderButtons extends Component {
    logoutHandler = (e) => {
        e.target.innerHTML = "Выходим...";
        this.props.history.push("/");
        this.props.logout();
    };
    render() {
        let buttons = this.props.is_auth ? (
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
                <li onClick={() => this.props.history.push("/personal_area")} className="register-button">
                    Личный кабинет
                </li>
                <li onClick={this.logoutHandler}>
                    <div className="menu-button">Выйти</div>
                    <div className="underline"/>
                </li>
            </ul>
        ) : (
            <ul className="buttons">
                <li onClick={() => this.props.history.push("/")}>
                    <div className="menu-button">Главная</div>
                    <div className="underline"/>
                </li>
                <li onClick={() => window.location = "/quests"}>
                    <div className="menu-button">Квесты</div>
                    <div className="underline"/>
                </li>
                <li onClick={() => this.props.history.push("/register")} className="register-button">
                    Зарегистрироваться
                </li>
            </ul>
        );
        return (
            <div>
                {buttons}
            </div>
        )
    }
}

export default HeaderButtons