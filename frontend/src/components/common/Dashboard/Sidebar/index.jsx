import React from 'react';
import './styles.css';

import { useAuth } from '../../../../providers/AuthProvider';
import Option from './Option';

const Sidebar = ({ isToolbar }) => {
  const { auth, logout } = useAuth();

  return (
    <div className={ `sidebar ${ isToolbar ? 'toolbar-open' : ''}` } >
      <div className="profile">
        <span className="icon-profile"></span>
        <p className="hello">Hello,</p>
        <p className="profile-name">{ auth.name }</p>
      </div>
      <div className="sidebar-options">
        <Option 
          icon={ 'suitcase' }
          name={ 'My Orders' }
        />
        <Option 
          icon={ 'user-settings' }
          name={ 'Account Settings' }
        />
        <Option 
          onClick={ () => logout() }
          icon={ 'user-logout' }
          name={ 'Logout' }
        />
      </div>
    </div>
  )
}

export default Sidebar;