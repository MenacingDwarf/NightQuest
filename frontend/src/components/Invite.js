import React, {Component} from 'react'

class Invite extends Component {
    render() {
        let invite = this.props.invite;
        return (
            <div>
                <h3>{invite.fields.title}</h3>
                Капитан: {invite.fields.captain}
                <div className="line"/>
            </div>
        )
    }
}

export default Invite