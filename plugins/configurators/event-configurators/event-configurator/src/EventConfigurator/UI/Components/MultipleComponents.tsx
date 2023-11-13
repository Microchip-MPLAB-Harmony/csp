import { GetSymbolLabelName } from '@mplab_harmony/harmony-plugin-core-service/build/database-access/SymbolAccess';
import { GetUIComponentWithOutLabel } from '@mplab_harmony/harmony-plugin-ui/build/components/Components';
import React from 'react';
import styles from './MultipleComponents.module.css';

const MultipleComponents = (props: {
  componentId: any;
  parentUpdate: () => void;
  symbolsArray: string[];
}) => {
  function updateValue() {
    props.parentUpdate();
  }

  function GetComponents() {
    return (
      <div className={styles['grid-container']}>
        {props.symbolsArray.map((object: string) => (
          <React.Fragment>
            <div>{GetSymbolLabelName(props.componentId, object)}</div>
            <GetUIComponentWithOutLabel
              key={object}
              componentId={props.componentId}
              symbolId={object}
              symbolListeners={[object]}
              onChange={updateValue}
            />
          </React.Fragment>
        ))}
      </div>
    );
  }
  return (
    <div>
      <div>
        <div className="p-fluid">
          <GetComponents />
        </div>
      </div>
    </div>
  );
};
export default MultipleComponents;
