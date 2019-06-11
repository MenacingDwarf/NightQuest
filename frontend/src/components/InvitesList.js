import React, {Component} from 'react'
import Invite from "./Invite";

class InvitesList extends Component {

    render() {
        console.log(this.props.invites);
        let invites = <div>Загрузка...</div>;
        if (this.props.invites !== null) {
            let invites_list = this.props.invites.map(invite => (
                <Invite invite={invite} key={invite.id}/>
            ));
            invites = this.props.invites.length > 0 ? (
                <div>
                    {invites_list}
                </div>
            ) : (
                <div>Новых приглашений нет</div>
            );
        }
        return (
            <div>
                {invites}
            </div>
        )
    }
}

export default InvitesList