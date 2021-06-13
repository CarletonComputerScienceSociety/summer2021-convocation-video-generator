import React from 'react';
import { data } from './data/data'

import * as htmlToImage from 'html-to-image';
import download from 'downloadjs'

function App() {
  console.log(data)

  function downloadImages() {
    let nodes = document.getElementsByClassName("group");

    for(let i = 0; i<nodes.length; i++) {
        downloadImage(nodes[i])
    }
  }

  function downloadImage(node) {
    htmlToImage.toPng(node)
        .then(function (dataUrl) {
            download(dataUrl, 'my-node.png');
        })
        .catch(function (error) {
            console.error('oops, something went wrong!', error);
        });
  }

  function downloadTargetImage(e) {
    htmlToImage.toPng(e.target.parentNode)
        .then(function (dataUrl) {
            download(dataUrl, 'my-node.png');
        })
        .catch(function (error) {
            console.error('oops, something went wrong!', error);
        });
}

  return (
    <div className="app">
        <button onClick={()=>downloadImages()}>Download Images</button>
       {
          data.map(group => (
            <div className="group" onClick={(e)=>downloadTargetImage(e)}>
                <div className="group-inner">
                {
                    group.map(student => (
                        <div className="student">
                            <div className="student-name">{student.fullname}</div>
                            <div className="student-titles">
                                <div className="student-title">{student.degree}</div>
                                {
                                    student.minors.map(minor => (
                                        <div className="student-title">{minor}</div>
                                    ))
                                }
                                { student.coop &&
                                    <div className="student-title">Co-operative Education</div>
                                }
                            </div>
                        </div>
                    ))
                }
                </div>
            </div>
          ))
        }
    </div>
  );
}

export default App;
