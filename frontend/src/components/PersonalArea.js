import React, {Component} from 'react'

class PersonalArea extends Component {
    render() {
        let form = <div>Пользователь не авторизован</div>;
        if (this.props.user_info) {
            let {first_name, last_name, email} = this.props.user_info;
            form = (
                <form action="/personal_area/" method={"post"}>
                    <label htmlFor="name">Ваше имя</label>
                    <input id="name" type="text" name="f_name" defaultValue={first_name}
                           placeholder="Введите имя"/>
                    <label htmlFor="last-name">Ваша фамилия</label>
                    <input id="last-name" type="text" name="l_name" defaultValue={last_name}
                           placeholder="Введите фамилию"/>
                    <label htmlFor="email">Ваша электронная почта</label>
                    <input id="email" type="email" name="email" defaultValue={email}
                           placeholder="Введите e-mail"/>
                    <input type="submit" className="register-button"
                           value="Сохранить изменения"/>
                </form>
            )
        }
        return (
            <div>
                <h4>ЛИЧНЫЙ КАБИНЕТ</h4>
                <div className="line"/>
                <div className="row">
                    <div className="col-6">
                        {form}
                    </div>
                </div>
            </div>
        )
    }
}

export default PersonalArea