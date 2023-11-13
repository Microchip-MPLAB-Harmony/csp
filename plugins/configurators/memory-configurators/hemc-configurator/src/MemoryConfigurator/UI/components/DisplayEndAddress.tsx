import { useState, useEffect } from 'react';
import {
  AddSymbolListener,
  GetSymbolValue,
} from '@mplab_harmony/harmony-plugin-core-service/build/database-access/SymbolAccess';
import { component_id } from '../MainView/MainBlock';
import { globalSymbolSStateData } from '@mplab_harmony/harmony-plugin-ui/build/components/Components';

const DisplayEndAddress = (props: { index: number }) => {
  const [endAddress, setEndAddress] = useState(
    GetSymbolValue(component_id, 'CS_' + props.index + '_END_ADDRESS')
  );

  useEffect(() => {
    globalSymbolSStateData.set('CS_' + props.index + '_END_ADDRESS', {
      changeValue: setEndAddress,
    });
    AddSymbolListener('CS_' + props.index + '_END_ADDRESS');
  }, []);

  return (
    <label style={{ fontSize: '1rem' }} className="p-col-fixed">
      {endAddress}
    </label>
  );
};

export default DisplayEndAddress;
