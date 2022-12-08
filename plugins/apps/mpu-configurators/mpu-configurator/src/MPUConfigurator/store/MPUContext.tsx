import React from 'react';

const MPUContext = React.createContext({
  MPUEnabled: false,
  updatePUEnabled: (checked: boolean) => {},
});

export default MPUContext;
