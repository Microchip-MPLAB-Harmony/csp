import React, { useState, useEffect } from 'react';
import {
  AddSymbolListener,
  GetSymbolValue,
} from '@mplab_harmony/harmony-plugin-core-service/build/database-access/SymbolAccess';
import { component_id } from '../MainView/MainBlock';
import { convertToBoolean } from '@mplab_harmony/harmony-plugin-core-service/build/database-access/SymbolUtils';
import { PrimeIcons } from 'primereact/api';
import { globalSymbolSStateData } from '@mplab_harmony/harmony-plugin-ui/build/components/Components';

const DisplayConflict = (prop: { index: number }) => {
  const [conflictStatus, setConflictStatus] = useState(
    convertToBoolean(
      GetSymbolValue(component_id, 'CS_' + prop.index + '_COMMENT')
    )
  );

  const isMemoryBankUsed = () => {
    const val = GetSymbolValue(
      component_id,
      'CS_' + prop.index + '_MEMORY_BANK_SIZE'
    );
    return val !== 'NOT_USED';
  };

  const [visible, setVisible] = useState(isMemoryBankUsed());

  const changeValue = (symbolValue: any) => {
    setConflictStatus(convertToBoolean(symbolValue));
  };

  useEffect(() => {
    globalSymbolSStateData.set('CS_' + prop.index + '_COMMENT', {
      changeValue: changeValue,
      setVisibilityStatus: setVisible,
    });
    AddSymbolListener('CS_' + prop.index + '_COMMENT');
  }, []);

  const getIconToDisplay = () => {
    if (!visible) {
      return <div></div>;
    }

    return conflictStatus ? (
      <div
        className={PrimeIcons.EXCLAMATION_CIRCLE}
        style={{ color: 'red' }}
      ></div>
    ) : (
      <div className={PrimeIcons.CHECK} style={{ color: 'green' }}></div>
    );
  };

  return <React.Fragment>{getIconToDisplay()}</React.Fragment>;
};

export default DisplayConflict;
