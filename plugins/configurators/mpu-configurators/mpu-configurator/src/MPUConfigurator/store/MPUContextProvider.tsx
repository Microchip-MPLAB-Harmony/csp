import React from 'react';
import MPUContext from './MPUContext';
import { GetSymbolValue } from '@mplab_harmony/harmony-plugin-core-service/build/database-access/SymbolAccess';
import { component_id } from 'MPUConfigurator/UI/MainView/MainBlock';
import { useState } from 'react';

const MPUContextProvider = (props: any) => {
  const [enabled, setEnabled] = useState(
    GetSymbolValue(component_id, 'CoreUseMPU')
  );

  const ctxt = {
    MPUEnabled: enabled,
    updatePUEnabled: setEnabled,
  };

  return (
    <MPUContext.Provider value={ctxt}>{props.children}</MPUContext.Provider>
  );
};

export default MPUContextProvider;
