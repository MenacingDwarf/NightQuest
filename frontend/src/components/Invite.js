import React, {Component} from 'react'

class Invite extends Component {
    render() {
        let invite = this.props.invite;
        return (
            <div>
                <div className={"invite-place"}>
                    <h3>{invite.team.title}</h3>
                    Капитан: {invite.team.captain}
                    <div className="line"/>
                </div>
                <div className={"invite-button"} onClick={() => window.location.href = "/teams/accept/invite/"+invite.id}>
                    <div className="button-content">Принять</div>
                    <div className="underline"/>
                </div>
            </div>
        )
    }
}

export default Invite