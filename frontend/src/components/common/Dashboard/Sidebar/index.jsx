import React from 'react';
import './styles.css';

import { useAuth } from '../../../../providers/AuthProvider';
import Option from './Option';

const Sidebar = () => {
  const { auth } = useAuth();

  return (
    <div className="sidebar">
      <div className="profile">
        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRvUSsKmg8eAXt7AMn4YNFMLROT_yLtb3kKjatqSL3FGTWkcxTC" />
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
          icon={ 'user-logout' }
          name={ 'Logout' }
        />
      </div>
    </div>
  )
}

export default Sidebar;