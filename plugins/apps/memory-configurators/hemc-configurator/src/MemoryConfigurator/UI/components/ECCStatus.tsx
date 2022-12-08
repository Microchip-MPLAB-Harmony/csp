import { useState, useEffect } from 'react';
import {
  AddSymbolListener,
  GetSymbolValue,
} from '@mplab_harmony/harmony-plugin-core-service/build/database-access/SymbolAccess';
import { component_id } from '../MainView/MainBlock';
import { globalSymbolSStateData } from '@mplab_harmony/harmony-plugin-ui/build/components/Components';

const ECCStatus = (props: { index: number }) => {
  const [ECCStatus, setECCStatus] = useState(
    GetSymbolValue(component_id, 'CS_' + props.index + '_HECC_ENABLE')
  );

  useEffect(() => {
    globalSymbolSStateData.set('CS_' + props.index + '_HECC_ENABLE', {
      changeValue: setECCStatus,
    });
    AddSymbolListener('CS_' + props.index + '_HECC_ENABLE');
  }, []);

  return (
    <label style={{ fontSize: '1rem' }} className="p-col-fixed">
      {ECCStatus === 'true' ? 'Enabled' : 'Disabled'}
    </label>
  );
};

export default ECCStatus;
