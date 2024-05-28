const PlainLabel = (props: {
  disPlayText: string;
  className: string;
  booldStatus?: boolean;
  toolTip?: string;
}) => {
  return (
    <div>
      <label
        style={{
          font: 'Calibri',
          fontSize: '14px',
          fontWeight: props.booldStatus ? 'bold' : 'initial'
        }}
        title={props.toolTip ? props.toolTip : props.disPlayText}
        className={props.className}>
        {props.disPlayText}
      </label>
    </div>
  );
};
export default PlainLabel;
