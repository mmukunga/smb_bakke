import React, { useState, useEffect } from 'react';
import axios from 'axios';

const Main = () => {

    const [imageURL, setImageURL] = useState(''); 
    const [selectedFile, setSelectedFile] = useState();
    const [isSelected, setIsSelected] = useState(false);

    var preview = document.getElementById('show-text');

    const changeHandler = (event) => {
        setSelectedFile(event.target.files[0]);
        setIsSelected(true);
    };

    const handleSubmission = async () => {
        const formData = new FormData();
        formData.append('file', selectedFile);

        await axios('/api/upload', {
            method: 'POST',
            body: formData,
            headers: { 
                "Content-Type": "multipart/form-data" 
            }
        }).then((response) => {
            const body = response.data;
            setImageURL(`http://localhost:3000/${selectedFile.name}`);
        }).catch((error) => {
            console.log({...error}) 
        });
    };

    return (
        <div style={{border:'solid 2px red', textAlign:'left', background:'#55acf3', padding:'2.5em', borderRadius:'1em'}}>
			<input type="file" name="file" onChange={changeHandler} />
            {isSelected ? (
				<div style={{width:'50%', textAlign:'center', textAlign:'left', border:'solid 2px green', background:'#99acf3', padding:'1.5em', borderRadius:'1em'}}>
					<p>Filename: {selectedFile.name}</p>
					<p>Filetype: {selectedFile.type}</p>
					<p>Size in bytes: {selectedFile.size}</p>
					<p>
						lastModifiedDate:{' '}
						{selectedFile.lastModifiedDate.toLocaleDateString()}
					</p>
				</div>
			) : (
				<p>Select a file to show details</p>
			)}
			<div>
				<button onClick={handleSubmission}>Submit</button>
			</div>
            <img src={imageURL} alt="img" />
            <span id='show-text'> Simon Image</span>
		</div>
      
    );
}

export default Main;