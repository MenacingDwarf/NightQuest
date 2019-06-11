import React, {Component} from 'react'

class Invite extends Component {
    render() {
        let invite = this.props.invite;
        return (
            <div>
                <h3>{invite.team.title}</h3>
                Капитан: {invite.team.captain}
                <div className="line"/>
            </div>
        )
    }
}

export default Invite