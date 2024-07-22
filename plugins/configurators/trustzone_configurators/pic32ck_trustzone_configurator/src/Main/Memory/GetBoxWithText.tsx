import { boxpaddingLeft, boxRightSideTempWidth, GetBox } from './Memory';

const GetBoxWithText = (props: {
  classCustom: any;
  displayText: any;
  color: any;
  boxHeight: any;
  hexDisplayText: any;
  textDisplayStatus: any;
}) => {
  return (
    <div className={props.classCustom}>
      {GetBox(
        props.displayText,
        props.color,
        props.boxHeight,
        boxpaddingLeft,
        props.textDisplayStatus
      )}
      {props.textDisplayStatus && (
        <div
          className='flex align-items-end justify-content-start text-gray-900 text-lg'
          style={{
            width: boxRightSideTempWidth + 'px',
            height: props.boxHeight + 'rem',
            paddingLeft: '5px'
          }}>
          {props.hexDisplayText}
        </div>
      )}
    </div>
  );
};
export default GetBoxWithText;
