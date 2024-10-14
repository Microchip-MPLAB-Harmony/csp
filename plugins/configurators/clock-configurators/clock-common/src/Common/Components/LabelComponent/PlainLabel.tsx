import { Tooltip } from 'primereact/tooltip';
import { useState } from 'react';
import { v4 as uuidv4 } from 'uuid';
const PlainLabel = (props: {
  disPlayText: string;
  className: string;
  booldStatus?: boolean;
  redColorStatus?: boolean;
  toolTip?: string;
}) => {
  const [tooltipClass] = useState(() => 'x' + uuidv4());
  return (
    <div>
      <Tooltip target={`.${tooltipClass}`} />
      <label
        style={{
          font: 'Calibri',
          fontSize: '14px',
          fontWeight: props.booldStatus ? 'bold' : 'initial',
          color: props.redColorStatus ? 'red' : 'black'
        }}
        className={`${tooltipClass} ${props.className ?? ''}`}
        data-pr-tooltip={props.toolTip ? props.toolTip : props.disPlayText}
        data-pr-position='bottom'>
        {props.disPlayText}
      </label>
    </div>
  );
};
export default PlainLabel;
